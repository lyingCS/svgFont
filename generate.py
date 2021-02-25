#conding=utf8
from myConfig import *
from myUtils import *
import os

cwd=os.getcwd()
os.chdir(ff_work_directory)
import fontforge
os.chdir(cwd)

def generate():
	newFont = fontforge.font()
	g = os.walk(svg_out_path)
	for path, dir_list, file_list in g:
		for file_name in file_list:
			[uni,name,wid]=file_name[:-4].split('_')
			newGlyph=newFont.createChar(int(uni),name)
			try:
				newGlyph.importOutlines(svg_out_path+'/'+file_name)
				newGlyph.width =int(wid)
			except FileNotFoundError:
				continue
	newFont.fullname = fontName
	newFont.familyname = fontName
	newFont.fontname = fontName
	# try:
	# 	os.remove(new_font_path)	
	# except FileNotFoundError:
	# 	pass
	newFont.generate(new_font_path)
	print('Generate successfully!')
if __name__=='__main__':
	generate()