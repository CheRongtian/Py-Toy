#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

# define SERVER_PORT 5432
# define MAX_LINE 256
# define MAX_PENDING 5

int main()
{
    struct sockaddr_in sin; // structure to hold the server's address info
    char buf[MAX_LINE]; // buffer to store incoming data
    int buf_len;
    socklen_t addr_len;
    int s, new_s;

    /* build address data structure */
    bzero((char *)&sin, sizeof(sin)); // clear memory
    sin.sin_family = AF_INET; // use Internet domain
    sin.sin_addr.s_addr = INADDR_ANY; // accept connections from any interface
    sin.sin_port = htons(SERVER_PORT); // convert port to network byte order

    /* setup passive open */
    if((s = socket(PF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("simplex-talk: bind");
        exit(1);
    }
    if((bind(s, (struct sockaddr *)&sin, sizeof(sin))) < 0)
    {
        perror("simplex-talk: socket");
        exit(1);
    }
    listen(s, MAX_PENDING);

    /* wait for connection, then receive and print text*/
    while(1)
    {
        addr_len = sizeof(sin);
        if((new_s = accept(s, (struct sockaddr *)&sin, &addr_len)) < 0)
        {
            perror("simplex-talk: accept");
            exit(1);
        }

        while((buf_len = recv(new_s, buf, sizeof(buf), 0)) > 0)
        {
            fputs(buf, stdout);
        }
        close(new_s);
    }

    return 0;
}