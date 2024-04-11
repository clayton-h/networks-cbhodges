//
// C socket program that provides
// IP addresses for a given hostname
//
// By: Clayton H.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>

int main(int argc, char *argv[])
{
    /*
    struct addrinfo {
    int              ai_flags;     // SEE ai_flags OPTIONS BELOW
    int              ai_family;    // AF_INET, AF_INET6, AF_UNSPEC
    int              ai_socktype;  // SOCK_STREAM, SOCK_DGRAM
    int              ai_protocol;  // use 0 for "any"
    size_t           ai_addrlen;   // size of ai_addr in bytes
    struct sockaddr *ai_addr;      // struct sockaddr_in or _in6
    char            *ai_canonname; // full canonical hostname

    struct addrinfo *ai_next;      // linked list, next node
    };
    */

    // Declare hints and results structs
    // (a linked list of type struct addrinfo)
    struct addrinfo hints, *res, *i;
    char ipstr[NI_MAXHOST];
    int status;

    // Check for required argc:
    // program name and hostname (2)
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s hostname\n", argv[0]);
        return 1;
    }

    // Empty the 'hints' struct and
    // set address structure preferences
    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;     // Specify any type of IP address
    hints.ai_socktype = SOCK_STREAM; // Specify TCP stream sockets

    /*
    int getaddrinfo(const char *node, // e.g. "www.example.com" or IP
                const char *service,  // e.g. "http" or port number
                const struct addrinfo *hints,
                struct addrinfo **res);
    */

    // Check if getaddrinfo() succeeded or failed
    if ((status = getaddrinfo(argv[1], NULL, &hints, &res)) != 0)
    {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(status));
        return 2;
    }

    // int getnameinfo(const struct sockaddr *sa, socklen_t salen,
    //                 char *host, size_t hostlen,
    //                 char *serv, size_t servlen, int flags);

    // Iterate through the linked-list and get human-readable (NI_NUMERICHOST)
    // IP addresses (stored in char ipstr[NI_MAXHOST]) for a given socket address (res)
    for (i = res; i != NULL; i = i->ai_next)
    {
        int error = getnameinfo(i->ai_addr, i->ai_addrlen, ipstr, sizeof(ipstr), NULL, 0, NI_NUMERICHOST);

        if (error != 0)
        {
            fprintf(stderr, "getnameinfo: %s\n", gai_strerror(error));
            continue;
        }

        fprintf(stdout, "IP address: %s\n\n", ipstr);
    }

    // Call freeaddrinfo to free the linked-list (res)
    freeaddrinfo(res);

    return 0;
}