from .listener import Listener
import asyncio

def kucoinProducer(queue):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Listener(queue).run(loop))