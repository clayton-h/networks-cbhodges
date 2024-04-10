import socket
import select

HOST = "127.0.0.1"
PORT = 1234
HEADERLENGTH = 10

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        socketList = [s]
        clients = {}
        print(f"Listening for connections on: {HOST}:{PORT}")

        while True:
            readSockets, _, exceptionSockets = select.select(socketList, [], socketList)

            for notifiedSocket in readSockets:
                if notifiedSocket == s:
                    conn, addr = s.accept()
                    socketList.append(conn)

                    try:
                        usernameHeader = conn.recv(HEADERLENGTH)
                        if not usernameHeader:
                            raise ValueError("No username header received")
                        usernameLength = int(usernameHeader.decode().strip())
                        username = conn.recv(usernameLength).decode().strip()
                        if not username:
                            raise ValueError("No username received")
                    except Exception as e:
                        print(f"Error receiving username from {addr}: {e}")
                        conn.close()
                        socketList.remove(conn)
                        continue

                    clients[conn] = username
                    print(f"Accepted new connection from {addr}, username: {username}")

                else:
                    try:
                        messageHeader = notifiedSocket.recv(HEADERLENGTH)
                        if not messageHeader:
                            raise ValueError("Client disconnected")
                        messageLength = int(messageHeader.decode().strip())
                        message = notifiedSocket.recv(messageLength).decode()
                    except ValueError:
                        print(f"Client {clients[notifiedSocket]} disconnected")
                        notifiedSocket.close()
                        socketList.remove(notifiedSocket)
                        del clients[notifiedSocket]
                        continue
                    except Exception as e:
                        print(f"Error receiving message from {clients[notifiedSocket]}: {e}")
                        notifiedSocket.close()
                        socketList.remove(notifiedSocket)
                        del clients[notifiedSocket]
                        continue

                    print(f"Received message from {clients[notifiedSocket]}: {message}")
                    for clientSocket in clients:
                        if clientSocket != notifiedSocket:
                            senderUsername = clients[notifiedSocket]
                            senderHeader = f"{len(senderUsername):<{HEADERLENGTH}}"
                            messageHeader = f"{len(message):<{HEADERLENGTH}}"
                            fullMessage = senderHeader + senderUsername + messageHeader + message
                            clientSocket.send(fullMessage.encode())

            for notifiedSocket in exceptionSockets:
                socketList.remove(notifiedSocket)
                del clients[notifiedSocket]

if __name__ == "__main__":
    main()
