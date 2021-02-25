#conding=utf8
from myConfig import *
from myUtils import *
import os

cwd=os.getcwd()
os.chdir(ff_work_directory)
import fontforge
os.chdir(cwd)

def export():
	F = fontforge.open(old_font_path)
	for name in F:
		index=str(F[name].unicode)
		width=str(F[name].width)
		filename = svg_path+'/'+index+'_'+name+'_'+width+'.'+ext
		F[name].export(filename)
	print('Export successfully!')
if __name__=='__main__':
	export()