from channels.generic.websocket import AsyncWebsocketConsumer

class Testserver(AsyncWebsocketConsumer):
    async def connect(self):
        await self.connect()


    async def disconnect(self,close_code):
        await self.disconnect()
    
    async def recive(self,data):
        print('>>>>  ',data)
        pass