import socket

target = "127.0.0.1"
port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto("MAYANK HERE",(target,port))
data, addr = client.recvfrom(4096)
print(data)
