from zmq import REP
from zmq.asyncio import Context
import asyncio
import msgpack


"""
Класс отвечает за получение сообщения от клиета
"""
class Server_REP:
    def __init__(self, socket_addr = "localhost", port = "5555"):
        self.context = Context()
        self.socket = self.context.socket(REP)
        self.socket.bind(f"tcp://{socket_addr}:{port}")

    """Функция отвечает за обработку получения сообщения"""
    async def handler_request(self):
        request = await self.socket.recv()
        data = msgpack.unpackb(request)
        return data
    
    """Функция отвечает за отправку ответа"""   
    async def send_responce(self, data):
        response = data
        await self.socket.send(msgpack.packb(response))

    """Закртие подключения"""
    async def close(self):
        self.socket.close()
        self.context.term()


async def main():
    server = Server_REP()
    while True:
        data = await server.handler_request()
        data += "5"
        await server.send_responce(data)



if __name__ == "__main__":
    asyncio.run(main())