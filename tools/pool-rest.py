
from multiprocessing import Process, Pool
import requests

def f(name):
    print('process -%d start' % name)
    url = 'http://101.200.174.136:10086/pvbyhh/04681ac0c1c04d0398bd8c5ee2e4703e/2016-07-26-00/2016-07-27-00'
    r = requests.get(url)
    print(r.status_code)
    print(r.text)
    return

if __name__ == '__main__':
    pool = Pool(processes = 10)
    for i in xrange(10):
        pool.apply_async(f, (i,))

    pool.close()
    pool.join()
