import zmq
import socket
import sys

ip = (socket.gethostbyname(socket.gethostname())).split('.')
ip = ip[0] + "." + ip[1] + "."

# Getting all class B IP's
name={}

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)

for j in range(256):
    x = ip + str(j) + '.'
    for i in range(256):
        ip_searchable = x + str(i)
        try:

            sock.connect("tcp:"+ip_searchable+":5678")

            # Send a "message" using the socket
            sock.send("Serena")

            if(sock.recv()):
                print(ip_searchable)

        except herror:
			pass
		# try:
		# 	up = socket.gethostbyaddr(add)[0]
		# 	if(name.has_key(up)):
		# 		print add+'--{'+name.get(up)+'} is up!'
		# 	else :
		# 		print socket.gethostbyaddr(up)
		# 		# print up+' is up!'
		# except herror:
		# 	pass
