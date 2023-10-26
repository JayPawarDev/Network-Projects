import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("127.0.0.1", 3000)

client_socket.connect(server_address)

client_socket.sendall(b"Hello Server. This is Client")

message = client_socket.recv(1024)

print("Message:", message)

client_socket.close()
