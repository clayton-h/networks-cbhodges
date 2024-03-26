/*
C Socket Server
*/

#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>

int main(int argc, char *argv)
{
    int serverSocket;

    serverSocket = socket(AF_INET, SOCK_STREAM, 0);

    printf("The socket number is: %d\n", serverSocket);

    while(1)
    {
        
    }
    close(serverSocket);

    return 0;
}