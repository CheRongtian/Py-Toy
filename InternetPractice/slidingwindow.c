#include "slidingwindow.h"
#include <stdint.h>
#include <stdbool.h>
#include <string.h>

void semWait(Semaphore *s);
void evCancel(Event e);
Event evSchedule(void (*handler)(void *), void *arg, int t);
void msgAddrHdr(Msg *m, char *hdr, int len);
void msgSaveCopy(Msg *dst, Msg *src);
void msgDestroy(Msg *m);
void semSignal(Semaphore *s);
char* msgStripHdr(Msg *m, int len);
void store_swp_hdr(SwpHdr hdr, char *buf);
void load_swp_hdr(SwpHdr *hdr, char *buf);
int swpSend(int link, Msg *m);
void deliver(int link, Msg *m);
void prepare_ack(Msg *m, int seq);
void swpTimeout(void *arg);
bool swpInWindow(uint8_t seqno, uint8_t min, uint8_t max);


static int
sendSWP(SwpState *state, Msg *frame)
{
    struct sendQ_slot *slot;
    char hbuf[HLEN];

    /* wait for send window to open */
    semWait(&state->sendWindowNotFull);
    state->hdr.SeqNum = ++ state->LFS;
    slot = &state->sendQ[state->hdr.SeqNum % SWS];
    store_swp_hdr(state->hdr, hbuf);
    msgAddrHdr(frame, hbuf, HLEN);
    msgSaveCopy(&slot->msg, frame);
    slot->timeout = evSchedule(swpTimeout, slot, SWP_SEND_TIMEOUT);
    return swpSend(LINK, frame);
}

static int
deliverSWP(SwpState *state, Msg *frame)
{
    SwpHdr hdr;
    char *hbuf;

    hbuf = msgStripHdr(frame, HLEN);
    load_swp_hdr(&hdr, hbuf);
    if(hdr.Flags & FLAG_ACK_VALID)
    {
        /* received an acknowledge-do SENDER side */
        if(swpInWindow(hdr.AckNum, state->LAR + 1, state->LFS))
        {
            do
            {
                struct sendQ_slot *slot;
                
                slot = &state->sendQ[++state->LAR % SWS];
                evCancel(slot->timeout);
                msgDestroy(&slot->msg);
                semSignal(&state->sendWindowNotFull);
            } while(state->LAR != hdr.AckNum);
        }
    }

    if(hdr.Flags & FLAG_HAS_DATA)
    {
        struct recvQ_slot *slot;
        
        /* received data packet-do RECEIVER side */
        slot = &state->recvQ[hdr.SeqNum % RWS];
        if(!swpInWindow(hdr.SeqNum, state->NFE, state->NFE +RWS -1))
        {
            // drop the message
            return SUCCESS;
        }
        msgSaveCopy(&slot->msg, frame);
        slot->received = TRUE;
        if(hdr.SeqNum == state->NFE)
        {
            Msg m;

            while(slot->received)
            {
                deliver(HLP, &slot->msg);
                msgDestroy(&slot->msg);
                slot->received = FALSE;
                slot = &state->recvQ[++state->NFE % RWS];
            }
            // send ACK: 
            prepare_ack(&m, state->NFE-1);
            swpSend(LINK, &m);
            msgDestroy(&m);
        }
    }
    return SUCCESS;
}

bool
swpInWindow(SwpSeqno seqno, SwpSeqno min, SwpSeqno max)
{
    SwpSeqno pos, maxpos;

    pos = seqno - min; // pos should be in rang [0, MAX]
    maxpos = max - min + 1; // maxpos is in range [0, MAX]
    return pos < maxpos;
}

int swpSend(int link, Msg *m) {
    return 0;
}
