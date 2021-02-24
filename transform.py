#conding=utf8
from myConfig import *
from myUtils import *
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


def process(ls, alpha, beta, a, b):
    #     print(dx,dy)
    for i in range(len(ls)):
        if ls[i][0] == 'q':
            dx = int(ls[i][3])
            dy = int(ls[i][4])
            ddx = (dx // alpha) * a
            ddy = (dy // alpha) * b
            ls[i][1] = str(int(ls[i][1]) + ddx)
            ls[i][2] = str(int(ls[i][2]) + ddy)
        elif ls[i][0] == 'h':
            dx = int(ls[i][1])
            dy = 0
            cx = dx // 2
            cy = (dx // beta) * b
            ls[i] = ['q', str(cx), str(cy), str(dx), str(dy)]
        elif ls[i][0] == 'v':
            dx = 0
            dy = int(ls[i][1])
            cx = (dy // beta) * a
            cy = dy // 2
            ls[i] = ['q', str(cx), str(cy), str(dx), str(dy)]
        elif (ls[i][0] == 'l'):
            dx = int(ls[i][1])
            dy = int(ls[i][2])
            cx = dx // 2 + (dx // beta) * a
            cy = dy // 2 + (dy // beta) * b
            ls[i] = ['q', str(cx), str(cy), str(dx), str(dy)]

    return ls


def list2xml(ls):
    ret = ""
    for i in ls:
        ret += " ".join(i)
    return ret


def glphyProcessing(s1, s2, alpha, beta, ls):
    tree = ET.parse(s1)
    old = tree.getroot()[0].attrib['d']
    num = int(s1.split('_')[0].split('/')[-1])
    n = len(ls[0])
    #     print(num,n,num%n)
    new = list2xml(process(path(old), alpha, beta, ls[0][num % n], ls[1][num % n]))
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


def allProcessing(sign, alpha, beta):
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
                    glphyProcessing(inPath, outPath, alpha, beta, signList)
                else:
                    res = open(inPath)
                    info = res.read()
                    des = open(outPath, 'w+')
                    des.write(info)
                    des.close()
                    res.close()
    print('Transform successfully!')


def getSign(s1, s2, alpha, sign):
    list1 = path(getInfo(s1))
    list2 = path(getInfo(s2))
    a = -1
    b = -1
    num = int(s1.split('_')[0].split('/')[-1])
    mp = {}
    for i in range(len(list1)):
        if list1[i][0] == 'q':
            dx = int(list1[i][3])
            dy = int(list2[i][4])
            ddx = int(list2[i][1]) - int(list1[i][1])
            ddy = int(list2[i][2]) - int(list1[i][2])
            if (dx // alpha) != 0:
                a = ddx / (dx // alpha)
            if (dy // alpha) != 0:
                b = ddy / (dy // alpha)
    n = (len(sign) / 2)
    if a != -1:
        sign[int(num % n)] = hex(int(a))[2:]
    if (b != -1):
        sign[int(num % n + n)] = hex(int(b))[2:]
    return sign



def oneByoneGetAllSign(alpha,n,sign,file_name):
    inPath=svg_path+'/'+file_name
    outPath=svg_out_path+'/'+file_name
    tree = ET.parse(outPath)
    root = tree.getroot()
    # print(file_name)
    if ('d' not in root[0].attrib.keys()):
        return -1
    sign = getSign(inPath,outPath, alpha,sign)
    if (sign.count("?") == 0):
        t = ''.join(sign)
        return t
    else:
        return sign
    # print(t)