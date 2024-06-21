import socket

s = socket.socket()

port = 8080
s.bind(('', port))
print("Socket binded to port %s" %(port))

s.listen(2) # allows 2 unaccepted connections
print("Server is listening")

while True:
    conn, addr = s.accept()
    print("Got connection from", addr)
    conn.send("Hello client".encode())

    data = conn.recv(1024).decode()
    print("Client response: " + data) 

    conn.close()
    break

# https://roadmap.sh/backend/project-ideas#7-real-time-polling-app
# https://roadmap.sh/backend/project-ideas#16-messaging-platform-backend