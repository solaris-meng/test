import qiniu
import sys
import os
import getopt

def get_files(path):
		
	file_list = []
		
	if os.path.isfile(path):
		file_list.append(path)
	elif os.path.isdir(path):
		dir_list = os.listdir(path)

		for each_node in dir_list:
			each_file = path + each_node
				
			if os.path.isfile(each_file):
				file_list.append(each_file)
			elif os.path.isdir(each_file):
				file_list = file_list + get_files(each_file)
			else:
				print("error in QiniuManage.get_files: " + each_file + " is not a file or dir")

	else:
		print("error in QiniuManage.get_files: " + path + " is not a file or dir")

	return file_list

class QiniuManage(object):

	"""
	qiniu interaction class
	"""

	def __init__(self, access_key, secret_key):
		self.__access_key = access_key
		self.__secret_key = secret_key
		print("init QiniuManage")


	def upload(self, path, bucket):
		file_list = get_files(path)
		q = qiniu.Auth(self.__access_key, self.__secret_key)

		for each_file in file_list:
			key = os.path.dirname(each_file) + os.path.basename(each_file)
			token = q.upload_token(bucket, key)
			ret, info = qiniu.put_file(token, key, each_file)
			if ret is not None:
				print(each_file + ' is uploaded')
			else:
				print(info)

