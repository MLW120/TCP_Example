import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 6000)
print('INICIANT')
s.bind(server_address)
s.listen(5) #Numero maxim de peticions pendens (a la cua)

while True:
	try:
		# Wait for a connection
		print('ESPERANT')
		connection, client_address = s.accept()
		try:
			print('connection from ' + str(client_address))
	
			# Receive the data in small chunks and retransmit it
			while True:
				data = connection.recv(1024)
				print('received "%s"' % data)
				if data:
					print('sending data back to the client')
					connection.sendall(data)
				else:
					print('no more data from', client_address)
					break
            
		finally:
			# Clean up the connection
			connection.close()
	except KeyboardInterrupt:
		break
