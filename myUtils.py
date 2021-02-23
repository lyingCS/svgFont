import hashlib
from myConfig import *
import os
def getDigest(key):
	return hashlib.md5(key.encode('utf-8')).hexdigest()
def cleanDir(path):
	try:
		os.mkdir(path)
	except FileExistsError:
		pass
	# pathList = os.listdir(path)
	# for file in pathList:
	# 	os.remove(path+'/'+file)