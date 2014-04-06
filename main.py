# Client Code
# import zmq
# import sys
#
# # ZeroMQ Context
# context = zmq.Context()
#
# # Define the socket using the "Context"
# sock = context.socket(zmq.REQ)
# sock.connect("tcp://127.0.0.1:5678")
#
# # Send a "message" using the socket
# sock.send(" ".join(sys.argv[1:]))
# print sock.recv()

# Server Code
# import zmq
#
# # ZeroMQ Context
# context = zmq.Context()
#
# # Define the socket using the "Context"
# sock = context.socket(zmq.REP)
# sock.bind("tcp://127.0.0.1:5678")
#
# # Run a simple "Echo" server
# while True:
#     message = sock.recv()
#     sock.send("Echo: " + message)
#     print "Echo: " + message

# Getting all class B IP's
# ip='160.39.'
# name={}
#
# for j in range(256):
# 	x = ip + str(j) + '.'
# 	for i in range(256):
# 		add = x + str(i)
# 		try:
#
# 		except herror:
# 			pass
# 		# try:
# 		# 	up = socket.gethostbyaddr(add)[0]
# 		# 	if(name.has_key(up)):
# 		# 		print add+'--{'+name.get(up)+'} is up!'
# 		# 	else :
# 		# 		print socket.gethostbyaddr(up)
# 		# 		# print up+' is up!'
# 		# except herror:
# 		# 	pass

# Check if port is open

# import socket;
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# result = sock.connect_ex(('127.0.0.1',80))
# if result == 0:
#    print "Port is open"
# else:
#    print "Port is not open"
#
#
