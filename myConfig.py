import pickle

fontName = "Myfont"
ff_work_directory = "D:/Program Files/FontForgeBuilds/bin"  #! change this into your bin path
key = "3312280576@qq.com"          # here key is just an email addr

ext='svg'
svg_path = "svg"
svg_out_path = "svg_out"
svg_ver_path = "svg_ver"

old_font_path='fz.ttf'
new_font_path='out.ttf'
verify_font_path='out.ttf'

with open('dalpha.dat', 'rb') as f:
    dalpha=pickle.load(f)
gama=10
# ask zcs for details about that