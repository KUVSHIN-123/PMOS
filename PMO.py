import zmq

def publisher_data():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind()