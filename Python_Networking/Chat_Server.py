import socket
import threading

def get_bind_ip_addr():
	bind_ip = raw_input('Enter the IP to bind the Server : ')
	return bind_ip

def handle_client(client_socket):
	data = client_socket.recv(4096)
	print ("[*] Recieved : %s"%data)
	client_socket.send('ACK')
	client_socket.close()


BIND_IP = get_bind_ip_addr()
CLIENTS = {}

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((BIND_IP,0))
server.listen(5)
print ("[*] Server Started... ")


print ("Give the Server details to your friends to start chatting...")
print ("SERVER ADDRESS : %s"%BIND_IP)
print ("SERVER PORT : %s "%server.getsockname()[1])

while True:
		client, addr = server.accept()
		print("[*] Accepted connection from: %s:%d"%(addr[0],addr[1]))
		client_handler = threading.Thread(target=handle_client,args=(client,))
		client_handler.start()



