def consumer(queue):
    while 1:
        item = queue.get()
        print(f"Received: {item}")