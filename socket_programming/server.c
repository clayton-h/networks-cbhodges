#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
    int serverSocket;
    int clientSocket;
    int setSockOptResult;
    int bindResult;
    int listenResult;
    int yes = 1;
    FILE *file;
    char *fileBuffer;
    size_t fileSize;
    size_t fileReadSize;

    struct addrinfo hints, *res;

    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flags = AI_PASSIVE;
    int status = getaddrinfo(NULL, "1234", &hints, &res);
    if (status != 0)
    {
        fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status));
        return 1;
    }

    struct sockaddr_in clientAddress;
    int addrSize = sizeof(struct sockaddr_storage);

    // Create socket
    serverSocket = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
    if (serverSocket == -1)
    {
        perror("Failed to create socket");
        freeaddrinfo(res);
        return 1;
    }
    printf("The socket number is: %d\n", serverSocket);

    // Set socket options
    setSockOptResult = setsockopt(serverSocket, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes));
    printf("setSockOptResult: %d\n", setSockOptResult);

    // Bind port to IP address
    bindResult = bind(serverSocket, res->ai_addr, res->ai_addrlen);
    printf("bindResult: %d\n", bindResult);

    // File IO
    file = fopen("test.txt", "rb");
    if (file == NULL)
    {
        perror("Failed to open file");
        close(serverSocket);
        freeaddrinfo(res);
        return 1;
    }
    fseek(file, 0, SEEK_END);
    fileSize = ftell(file);
    rewind(file);

    printf("The file size is: %d\n", fileSize);
    fileBuffer = (char *)malloc(fileSize * sizeof(char));
    if (fileBuffer == NULL)
    {
        perror("Failed to allocate memory for file buffer");
        fclose(file);
        close(serverSocket);
        freeaddrinfo(res);
        return 1;
    }
    fileReadSize = fread(fileBuffer, sizeof(char), fileSize, file);
    printf("Read in %d bytes to fileBuffer\n", fileReadSize);

    // Listen on port
    listenResult = listen(serverSocket, 5);
    printf("listenResult: %d\n", listenResult);

    // Accept connection
    clientSocket = accept(serverSocket, (struct sockaddr *)&clientAddress, (socklen_t *)&addrSize);
    printf("The client socket number is: %d\n", clientSocket);

    char buffer[1024] = {0};
    while (1)
    {
        ssize_t sendSize;
        ssize_t recvSize;
        sprintf(buffer, "%ld", fileSize);
        send(clientSocket, buffer, strlen(buffer), 0);

        memset(buffer, 0, strlen(buffer));
        recvSize = recv(clientSocket, buffer, 1024, 0);
        memset(buffer, 0, recvSize);
        sendSize = send(clientSocket, fileBuffer, fileSize, 0);
        recvSize = recv(clientSocket, buffer, 1024, 0);
        printf("Received from buffer: %s\n", buffer);

        break;
    }

    fclose(file);
    free(fileBuffer);
    close(serverSocket);
    freeaddrinfo(res);

    return 0;
}
