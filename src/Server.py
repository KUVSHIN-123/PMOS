from zmq import REP
from zmq.asyncio import Context
import asyncio
import pickle


"""
Класс отвечает за получение сообщения от клиета
"""
class Server:
    def __init__(self, socket_addr = "tcp://localhost:5555"):
        self.context = Context()
        self.socket = self.context.socket(REP)
        self.socket.bind(socket_addr)

    """Функция отвечает за обработку получения сообщения"""
    async def handler_request(self):
        request = await self.socket.recv()
        data = pickle.loads(request)
        return data
    
    """Функция отвечает за отправку ответа"""   
    async def send_responce(self, data):
        response = data
        await self.socket.send(pickle.dumps(response))

    """Закртие подключения"""
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