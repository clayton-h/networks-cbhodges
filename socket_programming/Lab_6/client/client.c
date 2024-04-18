#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define PORT 1234
#define SERVER_IP "127.0.0.1"

int main(int argc, char **argv)
{
    int client_fd;
    struct sockaddr_in server_addr;
    char buf[100];

    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <mode>\n", argv[0]);
        exit(1);
    }

    client_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (client_fd == -1)
    {
        perror("socket");
        return 1;
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);

    if (connect(client_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
    {
        perror("connect");
        return 2;
    }

    write(client_fd, argv[1], 1); // Send mode to server

    if (strcmp(argv[1], "1") == 0)
    {
        printf("Enter strings to echo ('close' to exit):\n");
        while (fgets(buf, sizeof(buf), stdin))
        {
            write(client_fd, buf, strlen(buf));
            if (read(client_fd, buf, sizeof(buf)) > 0)
            {
                printf("Echo from server: %s", buf);
            }
            if (strcmp(buf, "goodbye\n") == 0)
            {
                break;
            }
        }
    }
    else if (strcmp(argv[1], "2") == 0)
    {
        FILE *file = fopen("test.txt", "wb");
        int bytes_recv;
        while ((bytes_recv = read(client_fd, buf, sizeof(buf))) > 0)
        {
            fwrite(buf, 1, bytes_recv, file);
        }
        fclose(file);
        printf("File received and saved as 'test.txt'\n");
    }

    close(client_fd);
    return 0;
}