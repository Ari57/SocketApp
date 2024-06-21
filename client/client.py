import socket

port = 8080
host = "127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    message = input("Type message: ").encode()
    s.sendall(message)
    data = s.recv(1024).decode()
    
print(f"Server response: {data!r}")

# client should be able to send a message via keyboard input