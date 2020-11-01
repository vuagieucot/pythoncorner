import threading
import time

class myThread(threading.Thread):
    """
    Thread count down
    """
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self._threadId = threadId
        self._name = name
        self._count = count

    def run(self):
        print('Starting: {}\n'.format(self._name))
        print_time(self._name, 1, self._count)
        print('Exiting: {}\n'.format(self._name))

def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print('{0}: {1} {2}\n'.format(name, time.ctime(time.time()), count))
        count -=1

thread1 = myThread(1, 'Thread-1', 10)
thread2 = myThread(2, 'Thread-2', 5)
thread3 = myThread(3, 'Thread-3', 20)

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print('Finish main thread')
