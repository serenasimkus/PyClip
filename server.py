#
import zmq, sys

def Discoverable(name):

    # ZeroMQ Context
    context = zmq.Context()

    # Define the socket using the "Context"
    sock = context.socket(zmq.REP)
    sock.bind("tcp://*:5696")

    # Run a simple "Echo" server
    while True:
        message = sock.recv()
        sock.send(name)

Discoverable(sys.argv[0])
