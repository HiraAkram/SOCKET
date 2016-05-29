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
def getindexofc(port):
	k=0
        while k<n:
		if cl2[k]==port:
			return k
		k=k+1
	print 'not found port'

def getconn(conn):
	w=0
	while w<n:
		if c[w]==conn:
			return w
		w=w+1
	print 'not found'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    i=0
    j=0
    z=0
    q=0
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    while j<n:
        i=0
    	while i<n:
		c[j].send(cl2[i]+" ")
		i=i+1
	j=j+1
    #infinite loop so that function do not terminate and thread do not end

    while True:
        data=conn.recv(1024)
        ports,d=data.split("<<")
        z=getindexofc(ports)
        q=getconn(conn)
        if conn==c[q]:
            conn=c[z]
            conn.sendall(cl2[q]+">>"+d)
            conn=c[q]
        elif conn==c[z]:
            conn=c[q]
            conn.sendall(cl2[z]+">>"+d)
            conn=c[z]
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
