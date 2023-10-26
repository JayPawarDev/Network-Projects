import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("127.0.0.1", 3000)

server_socket.bind(server_address)

server_socket.listen()

connectionObject, address = server_socket.accept()

message = connectionObject.recv(1024)

print("Address:", str(address))
print("Message:", message)

connectionObject.sendall(b"Hi Client. This is the server.")

server_socket.close()
