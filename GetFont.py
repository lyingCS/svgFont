import os
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
	init()
	digest = getDigest(key)
	print("Your Key: "+key)
	print("Your Digest: "+digest)

	export()
	trans.allProcessing(digest,alpha,beta)
	generate()

	# verify(PythonPath,alpha)
	print("End!")
	exit(0)