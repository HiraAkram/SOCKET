'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *

n=0
c=[]
cl2=[]
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8565 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(3)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    i=0
    j=0
    k=0
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    while j<n:
        i=0
    	while i<n:
		c[j].send(cl2[i]+" ")
		i=i+1
	j=j+1
    conn=c[2]
    conn.send('enter option: ')
    d=conn.recv(1024)
    #infinite loop so that function do not terminate and thread do not end
    if d=='a':
    	while True:
        	data=conn.recv(1024)
        	if conn==c[0]:
            		conn=c[2]
            		conn.sendall(data)
            		conn=c[0]
        	elif conn==c[2]:
            		conn=c[0]
            		conn.sendall(data)
            		conn=c[2]
        	if not data: 
            		break
    elif d=='b':
        while True:
        	data=conn.recv(1024)
        	if conn==c[1]:
            		conn=c[2]
            		conn.sendall(data)
            		conn=c[1]
        	elif conn==c[2]:
            		conn=c[1]
            		conn.sendall(data)
            		conn=c[2]
        	if not data: 
            		break
    #came out of loop
    conn.close()
#now keep talking with the client
while 1:
    conn, addr=s.accept()
    c.append(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    cl2.append(str(addr[1]))
    n=n+1

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

s.close()
