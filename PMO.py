import zmq

def publisher_data():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://desktop-43mqlbj-1.netbird.cloud:2000")
    while True:
        data = input()
        message = f"testing_topic {data}"
        socket.send_string(message)
        print(f"Data: {data} send!")

def subscriber_data():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://desktop-43mqlbj-1.netbird.cloud:2000")
    socket.setsockopt_string(zmq.SUBSCRIBE,"testing_topic")
    while True:
        response = socket.recv_string()
        print(f"Response: {response}")
