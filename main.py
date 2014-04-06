import socket, sys

host = ''
port = 6767

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

while 1:
    client, address = s.accept()
    data = client.recv(size)
    data = data.rstrip("\n")

	print(data)

    client.close()

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
