from cex.kucoin import kucoinProducer
from consumer import consumer
from multiprocessing import Process, Queue
import time

if __name__ == "__main__":
    queue = Queue()

    producer_process = Process(target=kucoinProducer, args=(queue,))
    consumer_process = Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()
