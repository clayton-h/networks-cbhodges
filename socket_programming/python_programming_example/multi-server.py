import socket
import select

HOST="127.0.0.1"
PORT=1234

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        socketList = [s]
        clients = {}
        print(f"Listening for connections on: {HOST}:{PORT}")
        while True:
            readSockets, _, exceptionsSockets = select.select(socketList, [], socketList)
            for notifiedSocket in socketList:
                conn, addr = s.accept()
                socketList.append(conn)

                clients[conn] = 'test'
                print(f"Accepted new connection from {conn}, username: test")
            else:
                user = clients[notifiedSocket]
                print(f"Received message from {user}")
                recvMessage = conn.recv(1024).decode()
                print(f"Message received: {recvMessage}")
                for clientSocket in clients:
                    if clientSocket != notifiedSocket:
                        clientSocket.send(recvMessage.encoded())


if __name__ == "__main__":
    main()