#conding=utf8  
import os
from fontforge import *

FontName = "Myfont"
oldFont = open('./fz.ttf')
newFont = font()
for glyph in oldFont:
	if oldFont[glyph].isWorthOutputting():
		uni = oldFont[glyph].unicode
		name = oldFont[glyph].glyphname
		newGlyph=newFont.createChar(oldFont[glyph].unicode,oldFont[glyph].glyphname)
		try:
			newGlyph.importOutlines("./svg_out/"+str(uni)+"_"+name+".svg")
			newGlyph.width = oldFont[glyph].width
		except FileNotFoundError:
			continue
newFont.fullname = FontName
newFont.familyname = FontName
newFont.fontname = FontName
try:
	newFont.generate("out.ttf")
except FileExistsError as e:
	print(e)
	os.remove('out.ttf')
newFont.generate("out.ttf")
