import socket

target = "127.0.1.1"
port = 34937

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target,port))
client.send("Hello Mayank Here")
response = client.recv(10000)
print(response)


