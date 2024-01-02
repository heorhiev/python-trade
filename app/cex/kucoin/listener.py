import asyncio
import json
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient
import config


class Listener():
    def __init__(self, queue):
        self.queue = queue

    async def deal_msg(self, msg):
        print(msg)
        if msg['topic'] == '/market/ticker:MATIC-USDT':
            data = {
                "cex": "kucoin",
                "ticker": "MATIC-USDT",
                "price": msg["data"]["price"],
            }

            self.queue.put(json.dumps(data))

    async def run(self, loop):
        client = WsToken(key=config.kucoin['key'], secret=config.kucoin['secret'], passphrase=config.kucoin['passphrase'], is_sandbox=False, url='')

        ws_client = await KucoinWsClient.create(None, client, self.deal_msg, private=False)
        
        await ws_client.subscribe('/market/ticker:MATIC-USDT')

        while True:
            await asyncio.sleep(60, loop=loop)