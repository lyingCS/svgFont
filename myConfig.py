import sys
import inspect, os
scriptDir=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
fontName = "Myfont"
ff_work_directory = "D:/Program Files/FontForgeBuilds/bin"  #! change this into your bin path
key = "3312280576@qq.com"          # here key is just an email addr

ext='svg'
svg_path = scriptDir+"/svg"
svg_out_path = scriptDir+"/svg_out"
svg_ver_path = scriptDir+"/svg_ver"

old_font_path=scriptDir+'/fz.TTF'
new_font_path=scriptDir+'/out.ttf'
verify_font_path=scriptDir+'/out.ttf'

alpha = 20
beta = 30
gama = 10
# ask zcs for details about that

leng=len(sys.argv)
if(leng>1):
	key=sys.argv[1]
	fontName=key
if(leng>2):
	new_font_path=sys.argv[2]
	verify_font_path=sys.argv[2]
if(leng>3):
	alpha=sys.argv[3]
if(leng>4):
	beta=sys.argv[4]
if(leng>5):
	gama=sys.argv[5]