from zmq import  STREAM, IDENTITY
from zmq.asyncio import Context
import asyncio


class Client_STREAM:
    def __init__(self, identity=b"HOME", socket_addr="localhost", port="5555"):
        self.context = Context()
        self.socket = self.context.socket(STREAM)
        self.socket.connect(f"tcp://{socket_addr}:{port}")
        self.socket.setsockopt(IDENTITY, identity)

    async def send_message(self, data):
        await self.socket.send(data)

    async def reciv_message(self):
        identity, empty, message = await self.socket.recv_multipart()
        return message
    
    async def close(self):
        self.socket.close()
        self.context.term()


async def main():
    client = Client_STREAM()
    data = "5"
    await client.send_message(data)
    responce = await client.reciv_message()
    print(responce.decode('utf-8'))
        

if __name__ == "__main__":
    asyncio.run(main())

