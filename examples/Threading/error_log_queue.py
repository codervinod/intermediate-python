import sys
import time
import threading
import random
from Queue import Queue

q = Queue()

def log_thread():
    while True:
        message = q.get()
        slow_print(message)

def log(message, *args):
    message = message % args
    q.put(message)

def slow_print(message):
    for ch in message:
        sys.stdout.write(ch)
        time.sleep(0.01 * random.random())
        sys.stdout.flush()
    sys.stdout.write('\n')
    sys.stdout.flush()

def target(x):
    for y in range(4):
        log('(x,y) is (%d, %d)',x,y)

threads = [ threading.Thread(target=target, args=(x,))
            for x in range(4) ]
log_thread = threading.Thread(target=log_thread)
log_thread.setDaemon(True)
log_thread.start()
for t in threads:
    t.start()
time.sleep(5)
for t in threads:
    t.join()
