import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://*:5690")

# Run a simple "Echo" server
while True:
    message = sock.recv()
    sock.send("Serena")
    print message
