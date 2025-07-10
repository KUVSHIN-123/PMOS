from zmq import  STREAM
from zmq.asyncio import Context
import asyncio
import msgpack



class Server_STREAM:
    def __init__(self, socket_addr="*", port="5555"):
        self.context = Context()
        self.socket = self.context.socket(STREAM)
        self.socket.bind(f"tcp://{socket_addr}:{port}")

    async def reciv_message(self):
        while True:
            self.identity, data = await self.socket.recv_multipart()
            print(f"1{data}")
            data = msgpack.unpackb(data)
            print(f"2{data}")
            data = msgpack.packb(data)
            print(f"3{data}")
            await self.socket.send_multipart([self.identity, b"", data])
            # return data

    # async def send_message(self, data):
    #    data = msgpack.packb(data)
    #    print(f"3{data}")
    #    await self.socket.send_multipart([self.identity, b"", data])

    async def close(self):
        self.socket.close()
        self.context.term()


async def main():
    server = Server_STREAM()
    while True:
        await server.reciv_message()
        # await server.send_message(data)



if __name__ == "__main__":
    asyncio.run(main())
