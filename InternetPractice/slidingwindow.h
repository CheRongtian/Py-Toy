#ifndef SLIDINGWINDOW_H
#define SLIDINGWINDOW_H

#include <stdint.h>
#include <stdbool.h>
#include <string.h>

typedef struct {char data[256];} Msg;
typedef struct {} Semaphore;
typedef struct {} Event;

#define SWS 8
#define RWS 8
#define HLEN 8
#define LINK 1
#define HLP 2
#define FLAG_ACK_VALID 0x01
#define FLAG_HAS_DATA 0x02
#define SWP_SEND_TIMEOUT 1000
#define SUCCESS 0
#define TRUE 1
#define FALSE 0

typedef uint8_t SwpSeqno;

typedef struct {
    SwpSeqno SeqNum; // sequence number of this frame
    SwpSeqno AckNum; // ack of received frame
    uint8_t Flags; // up to 8 bits worth of flags
} SwpHdr;

typedef struct {
    /* sender side state; */
    SwpSeqno LAR; // seqno of last ACK received
    SwpSeqno LFS; // last frame sent
    Semaphore sendWindowNotFull;
    SwpHdr hdr; // pre-initialized header

    struct sendQ_slot {
        Event timeout; // event associated with send-timeout
        Msg msg;
    } sendQ[SWS];

    // receiver side state
    SwpSeqno NFE;
    struct recvQ_slot {
        int received; // is msg valid?
        Msg msg;
    } recvQ[RWS];
} SwpState;

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
int SwpSend(int link, Msg *m);
void deliver(int link, Msg *m);
void prepare_ack(Msg *m, int seq);
void swpTimeout(void *arg);
bool swpInWindow(uint8_t seqno, uint8_t min, uint8_t max);

#endif