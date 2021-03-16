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


def process(ls, a, b):
    #     print(dx,dy)
    for i in range(len(ls)):
        if ls[i][0] == 'q':
            dx = int(ls[i][3])
            dy = int(ls[i][4])
            ddx = (dx // alpha) * a
            ddy = (dy // alpha) * b
            ls[i][1] = str(int(ls[i][1]) + ddx+1)
            ls[i][2] = str(int(ls[i][2]) + ddy+1)
        elif ls[i][0] == 'h':
            dx = int(ls[i][1])
            dy = 0
            cx = dx // 2
            cy = (dx // beta) * b
            ls[i] = ['q', str(cx), str(-cy+1), str(dx), str(dy)]
        elif ls[i][0] == 'v':
            dx = 0
            dy = int(ls[i][1])
            cx = (dy // beta) * a
            cy = dy // 2
            ls[i] = ['q', str(cx+1), str(cy), str(dx), str(dy)]
        elif (ls[i][0] == 'l'):
            dx = int(ls[i][1])
            dy = int(ls[i][2])
            cx = dx // 2 + (dx // beta) * a
            cy = dy // 2 + (dy // beta) * b
            ls[i] = ['q', str(cx+1), str(cy+1), str(dx), str(dy)]

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
    #     print(num,n,num%n)
    new = list2xml(tilt(process(path(old), ls[0][num % n], ls[1][num % n]),0.2))
    # print(old,new)
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
            # print(file_name)
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
