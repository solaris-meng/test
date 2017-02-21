

import datetime
import random
from operator import itemgetter

def init_dict_arr(n):
    arr = []
    for i in range(1, n):
        item = {}
        item['name'] = 'aaaa'
        item['value'] = random.randint(1,100000)
        arr.append(item)
    return arr


if True:
    arr = init_dict_arr(100000)

    
    t1 = datetime.datetime.now()
    if True:
        rv = [n for n in arr if n['value'] > 3000 ]
        pass
    t2 = datetime.datetime.now()
    print((t2-t1))

    if True:
        rv = []
        for n in arr:
            if n['value'] > 3000:
                rv.append(n)
    t3 = datetime.datetime.now()
    print((t3-t2))

    for i in rv[0:5]:
        print(i)

