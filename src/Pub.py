import zmq
import asyncio
from CONFIG_addr import *
from serialize import *

class Pub():

    def __init__(self, ip_addr = "localhost", port = "2000", topic = "default_topic"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(f"tcp://{ip_addr}:{port}")
        self.topic = topic

    async def publisher_data(self,data):
        data_type,data_byte = await packing(data)
        _,topic_byte = await packing(self.topic)
        message = [topic_byte,data_type,data_byte]
        print(message)
        try:
            self.socket.send_multipart(message)
            return 1
        except:
            return 0 


async def main():
    publisher = Pub(muravei_desk)
    while True:
        data = input()
        result = await publisher.publisher_data(data)
        if result == 1:
            print(f"Data: {data} send!")
            pass
        else:
            print(f"Data not send!")
            pass

asyncio.run(main())