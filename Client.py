import socket
import sys

m = input('Which is the message? ')

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 6000)
print('connecting to %s port %s' % server_address)
s.connect(server_address)
try:
	# Send data
	message = m + '<EOF>'   # 'This is the message.  It will be repeated.'
	print('sending "%s"' % message)
	s.sendall(message.encode())

	data = s.recv(1024)

finally:
	print('closing socket')
	s.close()
