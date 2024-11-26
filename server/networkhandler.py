import socket
import threading
import json

MAX_CONNECTIONS = 254
messagepath = "message/message.json"

with open(messagepath, 'r') as file:
    messagejson = json.load(file)

def handle_client(conn, addr):
    print(f"New connection from: {addr}")
    
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received from {addr}: {data}")
            if data == "Hello, server! I'm about to disconnect.":
                conn.send(f"{messagejson}".encode())
#            response = f"Server received: {data}"
#            conn.send(response.encode())
        except Exception as e:
            print(f"Error handling client {addr}: {e}")
            break
    
    conn.close()
    print(f"Connection closed: {addr}")

def start_server():
    host = ''  # Listen on all available interfaces
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(MAX_CONNECTIONS)

    print(f"Server listening on port {port}")

    while True:
        try:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == '__main__':
    start_server()
