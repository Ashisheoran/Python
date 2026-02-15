import socket
import threading

HOST = '0.0.0.0'  # Accept all connections
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            nickname = nicknames[index]
            clients.remove(client)
            nicknames.remove(nickname)
            broadcast(f"❌ {nickname} left the chat.".encode('utf-8'))
            client.close()
            break

def receive():
    print(f"✅ Server is running on {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        print(f"🔌 Connected with {str(address)}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"👤 Nickname: {nickname}")
        broadcast(f"🟢 {nickname} joined the chat!".encode('utf-8'))
        client.send("✅ Connected to server!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()
