import datetime
from multiprocessing import Process
import time


def print_time():
  while True:
    print datetime.datetime.now()
    time.sleep(1)


def run_in_thread():
  t = Process(target=print_time)
  t.daemon = True
  t.start()
  time.sleep(10)
  t.terminate()


run_in_thread()
