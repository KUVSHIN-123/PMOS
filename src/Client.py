from zmq import REQ
from zmq.asyncio import Context
import asyncio
import pickle

"""
Класс отвечает за отправку запроса на сервер и получения ответа.
"""
class Client:
    def __init__(self, socket_addr = "tcp://localhost:5555"):
        self.context = Context()
        self.socket = self.context.socket(REQ)
        self.socket.connect(socket_addr)

    """Функция отвечает за отправку сообщений (форма данных любой)"""
    async def send_request(self, data):
        await self.socket.send(pickle.dumps(data))

    """Функия отвечается за получение ответа от сервера (формат данных любой)"""
    async def recv_responce(self):
        data = await self.socket.recv()
        responce = pickle.loads(data)
        return responce
    
    """Закртие подключения"""
    async def close(self):
        self.socket.close()
        self.context.term()


async def main():
    client = Client()
    data = "5 + "
    await client.send_request(data)
    responce = await client.recv_responce()
    print(responce)
        

if __name__ == "__main__":
    asyncio.run(main())