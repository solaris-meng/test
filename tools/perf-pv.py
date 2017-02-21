

import requests
import grequests
import datetime

r = requests.get('http://101.200.130.178/api/get/apicustomer')
appids = r.json()

urls = []
for a in appids:
    #url = 'http://101.200.174.136:10086/pvbyhh/%s/2016-8-16-0/2016-8-16-11' % a
    url = 'http://123.57.136.45/manualtools/realtime/json/%s/2016-7-26' % a
    urls.append(url)


print(datetime.datetime.now())
print(len(urls))
if True:
    rs = (grequests.get(u) for u in urls)

    rv = grequests.map(rs)
    for r in rv:
        print(r.status_code)
        print(r.json())
print(datetime.datetime.now())
