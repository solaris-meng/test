# -*- coding: utf-8 -*-
# flake8: noqa
import requests
import time

from qiniu import Auth

access_key = 'BYzCKUDMoPirtnxd-pEEE4lRdPcnsS-vgc2l0jmL'
secret_key = 'IwtT9Hi6v58D2mc1YlV2karuV3XilawgmWVgRAOa'

q = Auth(access_key, secret_key)

#有两种方式构造base_url的形式
bucket_domain = '7xs43b.com1.z0.glb.clouddn.com'
key='manual/2016-3-21/Amap-V764_1.apk'

base_url = 'http://%s/%s' % (bucket_domain, key)

#或者直接输入url的方式下载
#base_url = 'http://domain/key'

f=open('tmp.log', 'wb+')
#可以设置token过期时间
for i in range(0,10000):
    time.sleep(0.01)
    private_url = q.private_download_url(base_url, expires=3600)
    f.write(private_url)
    f.write('\n')

f.close()
#print(private_url)
#r = requests.get(private_url)
#assert r.status_code == 200



