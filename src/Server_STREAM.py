from zmq import  STREAM
from zmq.asyncio import Context
import asyncio


class Server_STREAM:
    def __init__(self, socket_addr="*", port="5555"):
        self.context = Context()
        self.socket = self.context.socket(STREAM)
        self.socket.bind(f"tcp://{socket_addr}:{port}")

    async def reciv_message(self):
        while True:
            self.identity, message = await self.socket.recv_multipart()
            return message

    async def send_message(self, data):
       await self.socket.send_multipart([self.identity, b"", data])

    async def close(self):
        self.socket.close()
        self.context.term()


async def main():
    server = Server_STREAM()
    while True:
        data = await server.reciv_message()
        await server.send_message(data)



if __name__ == "__main__":
    asyncio.run(main())
