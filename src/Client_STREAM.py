from zmq import  STREAM, IDENTITY
from zmq.asyncio import Context
import asyncio
import msgpack


class Client_STREAM:
    def __init__(self, identity=b"HOME", socket_addr="localhost", port="5555"):
        self.context = Context()
        self.socket = self.context.socket(STREAM)
        self.socket.connect(f"tcp://{socket_addr}:{port}")
        self.socket.setsockopt(IDENTITY, identity)

    async def send_message(self, data):
        packed_data = msgpack.packb(data)
        await self.socket.send_multipart([b"", packed_data])

    async def reciv_message(self):
        identity, data = await self.socket.recv_multipart()
        unpacked = msgpack.unpackb(data)
        return unpacked
    
    async def close(self):
        self.socket.close()
        self.context.term()


async def main():
    client = Client_STREAM()
    data = "5"
    await client.send_message(data)
    responce = await client.reciv_message()
    print(responce)
        

if __name__ == "__main__":
    asyncio.run(main())

