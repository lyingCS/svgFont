import os
import hashlib
import xml.etree.ElementTree as ET
import processFun

def init():
	svg_path = "./svg"
	svg_out_path = "./svg_out"
	pathList = os.listdir(svg_path)
	for file in pathList:
		os.remove(svg_path+'/'+file)
	pathList = os.listdir(svg_out_path)
	for file in pathList:
		os.remove(svg_out_path+'/'+file)

# def verify(PythonPath,alpha):
# 	init()
# 	Command = PythonPath+' '+'getVerFile.py'
# 	os.system(Command)
# 	print("start verifying")
# 	processFun.getAllSign(alpha,32)

if __name__ == '__main__':
	key = "abcd1223456@uestc.com"
	key_md5 = hashlib.md5(key.encode('utf-8')).hexdigest()
	print(key_md5)
	alpha = 30
	PythonPath = "ffpython\\python.exe"
	impofilePath = 'import.py'
	expofilePath = 'export.py'
	init()
	Command = PythonPath+' '+expofilePath
	os.system(Command)
	processFun.allProcessing(key_md5,alpha,60)
	Command = PythonPath+' '+impofilePath
	os.system(Command)
	print("success!")
	# verify(PythonPath,alpha)
	exit(0)



