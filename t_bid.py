

import time
import requests


words = [
    '导航',
    '导航地图',
    '导航系统下载',
    '手机导航',
    '语言导航',
]

for word in words:
    bid = 0.3
    while bid < 10.0:
        url = 'http://101.200.83.122:7011/getEstimatedDataByBid?word=%s&bid=%f&matchType=4' % (word, bid)
        try:
            r = requests.get(url, timeout=5)
            rr = r.json()
            data = rr['data'][0]['mobile']

            charge = data['charge']
            click = data['click']
            cpc = data['cpc']
            pv = data['pv']
            rank = data['rank']
            recBid = data['recBid']
            show = data['show']
            showRate = data['showRate']
            with open('test_bid.txt', 'w+') as fd:
                msg = 'word - %s, bid - %f, %s\n' % (word, bid, str(data))
                print(msg)
                fd.write(msg)
        except:
            pass
        bid += 0.2
        time.sleep(0.5)
        #break
