from myConfig import *
from myUtils import *
from transform import *
import os

cwd=os.getcwd()
os.chdir(ff_work_directory)
import fontforge
os.chdir(cwd)

def verify():
    fontInfo = ''
    key_md5 = getDigest(key)
    sign = ["?" for i in range(key_len)]
    F = fontforge.open(verify_font_path)
    for name in F:
        index=str(F[name].unicode)
        filename = svg_out_path+'/'+index+'_'+name+ '.'+ext
        file_name = index+'_'+name+ '.'+ext
        F[name].export(filename)
        result = oneByoneGetAllSign(alpha,key_len,sign,file_name)
        if result == -1:
            continue
        if type(result) == type('str'):
            fontInfo = result
            break
        else:
            sign = result
    if key_md5 == fontInfo:
        print(key_md5)
        print(fontInfo)
        print('Succeed!')
        return True
    else:
        print('Failed!')
        return False

if __name__ == '__main__':
    verify()