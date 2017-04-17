import multiprocessing
import numpy as np
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(processName)s (%(process)s): %(message)s')

log = logging.getLogger()

def main():
    pool = multiprocessing.Pool(6)
    pool.map(return_list, range(20))

def return_list(i):
    log = logging.getLogger()
    log.info('Calling return_list(%d)', i)
    return np.array([i] * 10)

if __name__ == '__main__':
    main()