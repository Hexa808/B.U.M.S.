import socket
import threading
import json
import time

MAX_CONNECTIONS = 254
messagepath = "message/message.json"

# Shared variable to hold the latest JSON data
messagejson = {}

# Function to periodically update the JSON data
def update_json():
    global messagejson
    while True:
        try:
            with open(messagepath, 'r') as file:
                messagejson = json.load(file)
            print("JSON file updated.")
        except Exception as e:
            print(f"Error reading JSON file: {e}")
        time.sleep(120)  # Wait for 120 seconds before updating again

def handle_client(conn, addr):
    print(f"New connection from: {addr}")
    
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received from {addr}: {data}")
            if data == "Hello, server! I'm about to disconnect.":
                # Send the latest JSON data to the client
                conn.send(json.dumps(messagejson).encode())
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
    # Start a separate thread to update the JSON file periodically
    json_update_thread = threading.Thread(target=update_json, daemon=True)
    json_update_thread.start()

    start_server()
