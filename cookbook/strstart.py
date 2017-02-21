

import datetime

t1 = datetime.datetime.now()
for i in range(0,10000):
    s1 = 'https://github.com/solaris-meng/yushan2/blob/master/baiduapi/views.py'
    r = s1.startswith('http://')
    r = s1.endswith('py')
t2 = datetime.datetime.now()
print((t2-t1))

t3 = datetime.datetime.now()
for i in range(0,10000):
    s1 = 'https://github.com/sfdasdasolaris-meng/yushan2/blob/master/baiduapi/views.py'
    r = (s1[:8] == 'http://')
    r = (s1[-3:] == '.py')
t4 = datetime.datetime.now()
print((t4-t3))
