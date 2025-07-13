import zmq
import asyncio
from CONFIG_addr import *
from serialize import *

class Sub():
    def __init__(self, ip_addr = "localhost", port = "2000", topic = "default_topic"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(f"tcp://{ip_addr}:{port}")
        self.socket.setsockopt_string(zmq.SUBSCRIBE,f"{topic}")
        self.topic = topic 

    async def subscriber_data(self):
        topic, message = self.socket.recv_multipart()
        response = deserialize(message)
        return topic.decode("utf-8"), response

async def main():
    subscriber = Sub()
    while True:
        topic, response = await subscriber.subscriber_data()
        print(f"Response: {response}")

asyncio.run(main())