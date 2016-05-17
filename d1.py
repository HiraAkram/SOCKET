import socket
import select
import string
import sys
port=int(sys.argv[2])
host=sys.argv[1]
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print 'Connected, send message please'
while 1:
	sl=[sys.stdin,s]
	read_sockets,write_sockets,error_sockets=select.select(sl,[],[])
	for socket in read_sockets:
		if socket==s:
			data=socket.recv(1024)
			if data:
				sys.stdout.write(data)
			else:
				print 'Disconnected'
				sys.exit()
            	else:
			message=sys.stdin.readline()
			s.send(message)
