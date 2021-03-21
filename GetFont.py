import os
import sys
from time import time
import xml.etree.ElementTree as ET
import transform as trans
from myConfig import *
from myUtils import *
from export import *
from generate import *
from verify import *

def init():
	cleanDir(svg_path)
	cleanDir(svg_out_path)
	cleanDir(svg_ver_path)

if __name__ == '__main__':
	# print(key,alpha,beta,gama)
	oT=time()
	init()
	print("Init: "+str(time()-oT))

	oT=time()
	digest = getDigest(key)
	print("Digest: "+str(time()-oT))

	# print("Your Key: "+key)
	print("Your Digest: "+digest)

	oT=time()
	export()
	print("Export: "+str(time()-oT))

	# digest=['0' for i in range(64)]
	oT=time()
	trans.allProcessing(digest)
	print("Transform: "+str(time()-oT))

	oT=time()
	generate()
	print("Generate: "+str(time()-oT))

	# oT=time()
	# verify()
	# print("Verify: "+str(time()-oT))

	print("End!")
	exit(0)