#
import zmq, socket, sys, multiprocessing, subprocess, time
from multiprocessing import Process, Manager

def main():
    ip = (socket.gethostbyname(socket.gethostname())).split('.')
    ip = ip[0] + "." + ip[1] + "."

    # Getting all class B IP's
    manager = Manager()
    name = manager.dict()
    processes = []
    result = []

    for j in range(256):
        x = ip + str(j) + '.'
        for i in range(256):
            ip_searchable = x + str(i)

            process = multiprocessing.Process(target = findOthers, args=[ip_searchable, name])
            process.start()
            processes.append(process)

    for process in processes:
        process.join()

    print name.values()

def findOthers(ip_searchable, name):
    # ZeroMQ Context
    context = zmq.Context()

    # Define the socket using the "Context"
    sock = context.socket(zmq.REQ)
    sock.setsockopt(zmq.LINGER, 0)

    sock.connect("tcp://"+ip_searchable+":5697")

    # Send a "message" using the socket
    sock.send("Serena")

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)
    if poller.poll(10*10): # 10s timeout in milliseconds
        client_name = sock.recv()
        if(client_name):
            computer = []
            computer.append(client_name)
            computer.append(ip_searchable)
            name[ip_searchable] = computer
        else:
            sock.close()

main()
