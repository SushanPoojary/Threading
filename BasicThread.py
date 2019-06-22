import threading
import time


class SashaMessenger(threading.Thread):

    def run(self):
        for _ in range(50):
            time.sleep(0.25)
            print(threading.currentThread().getName())


x = SashaMessenger(name='Send Messages.')
y = SashaMessenger(name='Message Delivered.')
z = SashaMessenger(name='Message Received ')
x.start()
y.start()
z.start()
