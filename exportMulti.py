#conding=utf8
from myConfig import *
from myUtils import *
import os
import threading

cwd=os.getcwd()
os.chdir(ff_work_directory)
import fontforge
os.chdir(cwd)

def export():
	F = fontforge.open(old_font_path)
	flag=True
	num=8
	jobs=[0 for i in range(num)]
	ite=F.__iter__()
	while(flag):
		j=num
		for i in range(num):
			try:
				name=ite.__next__()
				index=str(F[name].unicode)
				filename = svg_path+'/'+index+'_'+name+ '.'+ext
				th=threading.Thread(target=F[name].export,args=(filename,))
				jobs[i]=th
				th.start()
			except StopIteration:
				flag=False
				j=i
				break
		for i in range(j):
			jobs[i].join()
	# for name in F:
	# 	index=str(F[name].unicode)
	# 	filename = svg_path+'/'+index+'_'+name+ '.'+ext
	# 	F[name].export(filename)
	print('Export successfully!')
if __name__=='__main__':
	export()