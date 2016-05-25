import socket
from threading import Thread
import sys

port=int(sys.argv[2])
host=sys.argv[1]
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def recv():
    while True:
        data=s.recv(1024)
	if data=='end':
		break
        print data

Thread(target=recv).start()
while True:
    data=raw_input('other: ')
    s.send(data)

s.close()
