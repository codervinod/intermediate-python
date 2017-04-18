import datetime
from threading import Timer, Thread
import time


def print_time():
  print datetime.datetime.now()
  Timer(1, print_time).start()


def run_in_thread():
  t = Thread(target=print_time)
  t.setDaemon(True)
  t.start()
  time.sleep(10)


run_in_thread()
