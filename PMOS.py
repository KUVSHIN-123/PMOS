import zmq
import asyncio
from storage_names import *

class PMOS():

    async def __init__(self, ip_addr = "localhost", port = "2000", topic = "default_topic"):
        self.ip_address = ip_addr
        self.port = port
        self.topic = topic 

    async def publisher_data(self):
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind(f"tcp://{self.ip_address}:{self.port}")
        while True:
            data = input()
            message = f"{self.topic} {data}"
            socket.send_string(message)
            print(f"Data: {data} send!")

    async def subscriber_data(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(f"tcp://{self.ip_address}:{self.port}")
        socket.setsockopt_string(zmq.SUBSCRIBE,f"{self.topic}")
        while True:
            response = socket.recv_string()
            print(f"Response: {response}")

pmos = PMOS(muravei_desk)
asyncio.run(pmos.subscriber_data())