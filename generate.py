#conding=utf8
from myConfig import *
from myUtils import *
import os

cwd=os.getcwd()
#os.chdir(ff_work_directory)
import fontforge
os.chdir(cwd)

def generate():
	oldFont = fontforge.open(old_font_path)
	newFont = fontforge.font()
	for glyph in oldFont:
		if oldFont[glyph].isWorthOutputting():
			uni = oldFont[glyph].unicode
			name = oldFont[glyph].glyphname
			width= oldFont[glyph].width
			newGlyph=newFont.createChar(oldFont[glyph].unicode,oldFont[glyph].glyphname)
			newGlyph.importOutlines(svg_out_path+'/'+str(uni)+"_"+name+"_"+str(width)+'.'+ext)
			newGlyph.width = width
			# try:
			# 	newGlyph.importOutlines(svg_out_path+'/'+str(uni)+"_"+name+"_"+str(oldFont[glyph].width)+'.'+ext)
			# 	newGlyph.width = oldFont[glyph].width
			# except FileNotFoundError:
			# 	continue
	newFont.fullname = fontName
	newFont.familyname = fontName
	newFont.fontname = fontName
	# try:
	# 	os.remove(new_font_path)	
	# except FileNotFoundError:
	# 	pass
	cleanDir(os.path.dirname(new_font_path))
	newFont.generate(new_font_path)
	print('Generate successfully!')
if __name__=='__main__':
	generate()
