'''
    Simple socket server using threads
'''
 
import socket
import select
import sys
from thread import *

c=[] 
HOST=''   # Symbolic name meaning all available interfaces
PORT=5788 # Arbitrary non-privileged port
 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(2)
print 'Socket now listening'
c.append(s)
 
#Function for handling connections. This will be used to create threads
def clientthread(conn,message):
	for st in c:
		if st!=s and st!=socket:
			try:
				st.send(message)
			except:
				st.close()
                		c.remove(st)
while 1:
	read_sockets,write_sockets,error_sockets=select.select(c,[],[])
	for socket in read_sockets:
		if socket==s:
			conn, addr=s.accept()
			c.append(conn)
                        start_new_thread(clientthread,(conn,"client:[%s:%s]" % addr))
		else:
			data=socket.recv(1024)
                    	if data:
				clientthread(socket,str(socket.getpeername())+':'+data)                
		 	continue
s.close()

