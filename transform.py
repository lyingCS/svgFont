#conding=utf8
from myConfig import *
from myUtils import *
from beautify import *
import xml.etree.ElementTree as ET
import os

def getInfo(text):
    tree = ET.parse(text)
    return tree.getroot()[0].attrib['d']

def path(s):
    ret = [['M']]
    lasi = 1
    for i in range(1, len(s)):
        if (s[i] >= 'A' and s[i] <= 'z'):
            ret[-1] += s[lasi:i].strip().split(' ')
            ret.append([s[i]])
            lasi = i + 1
    return ret


def process(ls, a, b, c, d):
    for i in range(len(ls)):
        if ls[i][0] == 'q':
            dx = eval(ls[i][3])
            dy = eval(ls[i][4])
            ddx = (dx // alpha) * a//2
            ddy = (dy // alpha) * b//2
            ls[i][1] = str(eval(ls[i][1]) + ddx)
            ls[i][2] = str(eval(ls[i][2]) + ddy)
        elif ls[i][0] == 'h':
            dx = eval(ls[i][1])
            dy = 0
            cx1 = dx // (2+d)
            cx2=dx-cx1
            cy1 = (dx // beta) * (b-8)
            cy2=-cy1
            ls[i] = ['q',str(cx1), str(cy1),str(dx//2), str(dy)]
            ls.insert(i+1, ['q',str(cx2-dx//2), str(cy2),str(dx-dx//2), str(dy)])
            i=i+1
        elif ls[i][0] == 'v':
            dx = 0
            dy = eval(ls[i][1])
            cx1 = (dy // beta) * (a-8)
            cx2=-cx1
            cy1 = dy // (2+c)
            cy2 = dy-cy1
            ls[i] = ['q', str(cx1), str(cy1),str(dx), str(dy//2)]
            ls.insert(i+1,['q', str(cx2),str(cy2-dy//2),str(dx), str(dy-dy//2)])
            i=i+1
        elif (ls[i][0] == 'l'):
            dx = eval(ls[i][1])
            dy = eval(ls[i][2])
            cx = dx // 2 + (dx // beta) * a//2
            cy = dy // 2 + (dy // beta) * b//2
            ls[i] = ['q', str(cx), str(cy), str(dx), str(dy)]

    return ls

def list2xml(ls):
    ret = ""
    for i in ls:
        ret += " ".join(i)
    return ret


def glphyProcessing(s1, s2, ls):
    tree = ET.parse(s1)
    old = tree.getroot()[0].attrib['d']
    num = int(s1.split('_')[0].split('/')[-1])
    n = len(ls[0])
    partition=num%n
    partition2=(partition+1)%n
    partition3=(partition+2)%n
    partition4=(partition+3)%n
    partition5=(partition+4)%n
    old_path=path(old)
    prolong(old_path,ls[0][partition3]*2,num)
    process(old_path, ls[0][partition], ls[1][partition], ls[0][partition2], ls[1][partition2])
    #thin(old_path, 0.8)
    #flat(old_path, 0.8)
    tilt(old_path, 0.2)
    new = list2xml(old_path)
    tree.getroot()[0].attrib['d'] = new
    tree.write(s2)


def sign2ls(s):
    n = len(s)
    lsx = []
    lsy = []
    for i in range(int(n / 2)):
        lsx.append(int(s[i], 16))
    for i in range(int(n / 2), n):
        lsy.append(int(s[i], 16))
    return [lsx, lsy]


def allProcessing(sign):
    g = os.walk(svg_path)
    signList = sign2ls(sign)
    for path, dir_list, file_list in g:
        for file_name in file_list:
            inPath=svg_path+'/'+file_name
            outPath=svg_out_path+'/'+file_name
            tree = ET.parse(inPath)
            root = tree.getroot()
            for child in root:
                if ('d' in child.attrib.keys()):
                    glphyProcessing(inPath, outPath,signList)
                else:
                    res = open(inPath)
                    info = res.read()
                    des = open(outPath, 'w+')
                    des.write(info)
                    des.close()
                    res.close()
    print('Transform successfully!')
