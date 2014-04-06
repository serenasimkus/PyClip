import zmq, socket, sys

ip = (socket.gethostbyname(socket.gethostname())).split('.')
ip = ip[0] + "." + ip[1] + "."

# Getting all class B IP's
name = []

for j in range(194, 195):
    x = ip + str(j) + '.'
    for i in range(256):
        ip_searchable = x + str(i)
        
        # ZeroMQ Context
        context = zmq.Context()

        # Define the socket using the "Context"
        sock = context.socket(zmq.REQ)
        sock.setsockopt(zmq.LINGER, 0)

        sock.connect("tcp://"+ip_searchable+":5690")

        # Send a "message" using the socket
        sock.send("Serena")

        poller = zmq.Poller()
        poller.register(sock, zmq.POLLIN)
        if poller.poll(10*10): # 10s timeout in milliseconds
            if(sock.recv()):
                name.append(ip_searchable)
            else:
                sock.close()


print name
