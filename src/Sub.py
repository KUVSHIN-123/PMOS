import zmq
import asyncio
from CONFIG_addr import *

class Sub():

    def __init__(self, ip_addr = "localhost", port = "2000", topic = "default_topic"):
        self.ip_address = ip_addr
        self.port = port
        self.topic = topic 

    async def subscriber_data(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(f"tcp://{self.ip_address}:{self.port}")
        socket.setsockopt_string(zmq.SUBSCRIBE,f"{self.topic}")
        response = socket.recv_string()
        return response

async def main():
    subscriber = Sub(muravei_desk)
    while True:
        response = await subscriber.subscriber_data()
        print(f"Response: {response}")