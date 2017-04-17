import sys
import time
import threading
import random

log_mutex = threading.Lock()

def log(message, *args):
    with log_mutex:
        slow_log(message, *args)

def slow_log(message, *args):
    message = message % args
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

for t in threads:
    t.start()
