import socket



def connect_and_close():
    host = '10.0.0.62'  # Server's hostname or IP address
    port = 5000         # The port used by the server

    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((host, port))
            print(f"Connected to {host}:{port}")

            # Send a message
            message = "Hello, server! I'm about to disconnect."
            s.sendall(message.encode())
            print(f"Sent: {message}")

            # Receive the response (optional)
            data = s.recv(1024).decode()
            print(f"Received: {data}")



            # The connection will be closed automatically when exiting the 'with' block
        
        print("Connection closed")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    connect_and_close()
