import threading


class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(20000):
            print(threading.current_thread().getName())

x = BuckysMessenger(name='Send out messages')
y = BuckysMessenger(name='Receive messages')
x.start()
y.start()