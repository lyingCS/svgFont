import hashlib
from myConfig import *
import os
from gmssl import sm3
# def getDigest(key):
# 	return hashlib.md5(key.encode('utf-8')).hexdigest()
def getDigest(key):
	return sm3.sm3_hash(sm3.str2byte(key))
	
def cleanDir(path):
	try:
		os.mkdir(path)
	except FileExistsError:
		pass
	# pathList = os.listdir(path)
	# for file in pathList:
	# 	os.remove(path+'/'+file)