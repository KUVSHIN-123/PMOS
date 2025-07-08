from zmq import REP
from zmq.asyncio import Context
import asyncio
import pickle

class Server:
    def __init__(self, socket_addr = "tcp://localhost:5555"):
        self.context = Context()
        self.socket = self.context.socket(REP)
        self.socket.bind(socket_addr)

    async def handler_request(self):
        request = await self.socket.recv()
        data = pickle.loads(request)
        return data
            
    async def send_responce(self, data):
        response = data
        await self.socket.send(pickle.dumps(response))

    async def close(self):
        self.socket.close()
        self.context.term()


async def main():
    server = Server()
    while True:
        data = await server.handler_request()
        data += "5"
        await server.send_responce(data)



if __name__ == "__main__":
    asyncio.run(main())