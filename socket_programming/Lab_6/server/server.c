#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>

#define PORT 1234
#define MAXSIZE 100

void handle_echo_mode(int client_fd);
void handle_file_transfer_mode(int client_fd);

int main(void)
{
    int server_fd, client_fd;                    // Listen on server_fd, new connection on client_fd
    struct sockaddr_in server_addr, client_addr; // Server/client address information
    socklen_t sin_size = sizeof(struct sockaddr_in);
    char mode_buf[2]; // Buffer for mode

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1)
    {
        perror("socket");
        return 1;
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
    {
        perror("bind");
        return 2;
    }

    listen(server_fd, 10);

    while (1)
    {
        client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &sin_size);
        if (client_fd == -1)
        {
            perror("accept");
            continue;
        }

        read(client_fd, mode_buf, 1);
        if (mode_buf[0] == '1')
        {
            handle_echo_mode(client_fd);
        }
        else if (mode_buf[0] == '2')
        {
            handle_file_transfer_mode(client_fd);
        }

        close(client_fd);
    }

    return 0;
}

void handle_echo_mode(int client_fd)
{
    char buf[MAXSIZE];
    while (read(client_fd, buf, MAXSIZE - 1) > 0)
    {
        buf[strcspn(buf, "\n")] = 0; // Remove newline character
        if (strcmp(buf, "close") == 0)
        {
            write(client_fd, "goodbye", 7);
            break;
        }
        else
        {
            write(client_fd, buf, strlen(buf));
        }
    }
}

void handle_file_transfer_mode(int client_fd)
{
    FILE *file = fopen("test.txt", "rb");
    char file_buf[256];
    int bytes_read;

    if (file == NULL)
    {
        perror("File opening failed");
        return;
    }

    while ((bytes_read = fread(file_buf, 1, sizeof(file_buf), file)) > 0)
    {
        write(client_fd, file_buf, bytes_read);
    }

    fclose(file);
}