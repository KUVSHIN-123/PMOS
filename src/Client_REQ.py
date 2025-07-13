from zmq import REQ
from zmq.asyncio import Context
import asyncio
from serialize import *

"""
Класс отвечает за отправку запроса на сервер и получения ответа.
"""
class ClientREQ:
    def __init__(self, socket_addr = "localhost", port = "5555"):
        self.context = Context()
        self.socket = self.context.socket(REQ)
        self.socket.connect(f"tcp://{socket_addr}:{port}")

    """Функция отвечает за отправку сообщений (форма данных любой)"""
    async def send_request(self, data):
        await self.socket.send(serialize(data))

    """Функия отвечается за получение ответа от сервера (формат данных любой)"""
    async def recv_responce(self):
        data = await self.socket.recv()
        responce = deserialize(data)
        return responce
    
    """Закртие подключения"""
    async def close(self):
        self.socket.close()
        self.context.term()


async def main():
    client = ClientREQ()
    data = "5 + "
    await client.send_request(data)
    responce = await client.recv_responce()
    print(responce)
        

if __name__ == "__main__":
    asyncio.run(main())