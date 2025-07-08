import zmq
import asyncio
from storage_names import *

class Pub():

    def __init__(self, ip_addr = "localhost", port = "2000", topic = "default_topic"):
        self.ip_address = ip_addr
        self.port = port
        self.topic = topic 

    async def publisher_data(self,data):
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind(f"tcp://{self.ip_address}:{self.port}")
        message = f"{self.topic} {data}"
        socket.send_string(message)
        print(f"Data: {data} send!")

async def main():
    publisher = Pub(muravei_desk)
    while True:
        data = input()
        await publisher.publisher_data(data)

asyncio.run(main())