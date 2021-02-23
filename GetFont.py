import os
from time import time
import xml.etree.ElementTree as ET
import transform as trans
from myConfig import *
from myUtils import *
from export import *
from generate import *

def init():
	cleanDir(svg_path)
	cleanDir(svg_out_path)
# def verify(PythonPath,alpha):
# 	init()
# 	Command = PythonPath+' '+'getVerFile.py'
# 	os.system(Command)
# 	print("start verifying")
# 	processFun.getAllSign(alpha,32)

if __name__ == '__main__':
	oT=time()
	init()
	print("Init: "+str(time()-oT))

	oT=time()
	digest = getDigest(key)
	print("Digest: "+str(time()-oT))

	# print("Your Key: "+key)
	# print("Your Digest: "+digest)

	oT=time()
	export()
	print("Export: "+str(time()-oT))

	oT=time()
	trans.allProcessing(digest,alpha,beta)
	print("Transform: "+str(time()-oT))

	oT=time()
	generate()
	print("Generate: "+str(time()-oT))

	# verify(PythonPath,alpha)
	print("End!")
	exit(0)