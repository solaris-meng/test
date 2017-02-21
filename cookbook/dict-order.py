

import random
from operator import itemgetter

def init_dict_arr(n):
    arr = []
    for i in range(1, n):
        item = {}
        item['name'] = 'aaaa'
        item['value'] = random.randint(1,10000)
        arr.append(item)
    return arr


if True:
    arr = init_dict_arr(10000)
    rv = sorted(arr, key=itemgetter('value'))

    for i in rv[0:30]:
        print(i)

