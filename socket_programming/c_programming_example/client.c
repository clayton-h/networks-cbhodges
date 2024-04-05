/*
C Socket Client
*/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <fcntl.h>
#include <sys/stat.h>

int main(int argc, char **argv)
{
    int socketNum;
    int inetStatus = 0;
    int connnectStatus;
    size_t fileSize;
    int fileDes;

    struct sockaddr_in address;

    // address.sin_addr.s_addr = INADDR_ANY; // 127.0.0.1
    inet_pton(AF_INET, "127.0.0.1", &address.sin_addr);
    printf("inetStatus: %d\n", inetStatus);

    address.sin_family = AF_INET;
    address.sin_port = htons(1234);

    // Create socket
    socketNum = socket(AF_INET, SOCK_STREAM, 0);

    connnectStatus = connect(socketNum, (struct sockaddr *)&address, sizeof(address));
    printf("connectStatus: %d\n", connnectStatus);

    char buffer[1024] = {0};
    int recvBytes;
    int readBytes;
    int sentBytes;
    while (1)
    {
        fileDes = open("clientRecvFile", O_RDWR | O_CREAT | O_TRUNC, S_IRWXU);
        recvBytes = recv(socketNum, buffer, 1024, 0);
        fileSize = atoi(buffer);
        memset(buffer, 0, recvBytes);
        sprintf(buffer, "Received Size");
        sentBytes = send(socketNum, buffer, strlen(buffer), 0);
        memset(buffer, 0, sentBytes);

        int offset = 0;
        while (offset < fileSize)
        {
            recvBytes = recv(socketNum, buffer, 1024, 0);
            offset += recvBytes;
            write(fileDes, buffer, recvBytes);
            memset(buffer, 0, recvBytes);
        }
        close(fileDes);

        // printf("What do you wanna send to the server?\n");
        // readBytes = read(1, buffer, sizeof(buffer));
        // read(1, buffer, sizeof(buffer));
        // printf("buffer: %s\n", buffer);
        // send(socketNum, buffer, sizeof(buffer), 0);

        // recvBytes = recv(socketNum, buffer, sizeof(buffer), 0);
        // printf("buffer: %s\n", buffer);

        // memset(buffer, 0, sizeof(buffer));
    }

    return 0;
}
