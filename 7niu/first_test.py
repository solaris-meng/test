import qiniu_manage
import sys
import os

if len(sys.argv) < 2:
    print('more args')
    os.exit()
else:
    upload_path = sys.argv[1]
    print('upload %s' % upload_path)

access_key = 'BYzCKUDMoPirtnxd-pEEE4lRdPcnsS-vgc2l0jmL'
secret_key = 'IwtT9Hi6v58D2mc1YlV2karuV3XilawgmWVgRAOa'
bucket_name = 'moushi-yushan-test-bucket'
#upload_path = '../Pack/new_apks/'

q = qiniu_manage.QiniuManage(access_key, secret_key)
q.upload(upload_path, bucket_name)

print('test is done')
