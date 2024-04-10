import socket
import errno
import sys

HOST = "127.0.0.1"
PORT = 1234
HEADERLENGTH = 10

def main():
    username = input("Enter your username: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.setblocking(False)

        usernameHeader = f"{len(username):<{HEADERLENGTH}}"
        client.send(f"{usernameHeader}{username}".encode())

        while True:
            message = input(f"{username} > ")
            if message:
                messageHeader = f"{len(message):<{HEADERLENGTH}}"
                fullMessage = messageHeader + message
                client.sendall(fullMessage.encode())

            try:
                while True:
                    senderHeader = client.recv(HEADERLENGTH)
                    if not senderHeader:
                        print("Connection closed by the server")
                        sys.exit()
                    senderLength = int(senderHeader.decode().strip())
                    sender = client.recv(senderLength).decode()

                    messageHeader = client.recv(HEADERLENGTH)
                    messageLength = int(messageHeader.decode().strip())
                    message = client.recv(messageLength).decode()

                    print(f"{sender} > {message}")
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print(f"Reading error: {str(e)}")
                    sys.exit()
                continue

if __name__ == "__main__":
    main()
