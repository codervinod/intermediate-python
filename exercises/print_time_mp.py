import datetime
from multiprocessing import Process, Value
import time


def print_time(should_exit):
  while should_exit.value == 0:
    print datetime.datetime.now()
    time.sleep(1)
  print "exiting"

def run_in_thread():
  should_exit = Value("i", 0)
  t = Process(target=print_time, args=(should_exit,))
  t.daemon = True
  t.start()
  time.sleep(10)
  should_exit.value = -1
  time.sleep(2)


run_in_thread()
