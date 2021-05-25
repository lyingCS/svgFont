#conding=utf8
from myConfig import *
from myUtils import *
from beautify import *
import xml.etree.ElementTree as ET
import os

def getInfo(text):
    #该函数根据文件名字符串得到字形的信息
    tree = ET.parse(text)
    return tree.getroot()[0].attrib['d']

def path(s):
    #该函数解析getInfo得到的x字形信息把每一条指令分开放到一个List中
    ret = [['M']]
    lasi = 1
    for i in range(1, len(s)):
        if (s[i] >= 'A' and s[i] <= 'z'):
            ret[-1] += s[lasi:i].strip().split(' ')
            ret.append([s[i]])
            lasi = i + 1
    return ret

def process(ls, a, b, c, d, e, f):
    #该函数对path函数d操作得到的List进行变换得到变换后的List
    i=0
    while i < len(ls):
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
            if e>8:
                cx1 = dx // (3+d)
                cy1 = (dx // beta) * (b-8)
                if abs(cy1)>abs(cx1):
                    cy1=(b-8)/abs(b-8)*cx1
                cx2=dx-cx1
                cy2=-cy1
                ls[i] = ['q',str(cx1), str(cy1),str(dx//2), str(dy)]
                ls.insert(i+1, ['q',str(cx2-dx//2), str(cy2),str(dx-dx//2), str(dy)])
                i=i+1
            else:
                if dx>0:
                    cx=dx*(e+1)/10
                else:
                    cx=dx-dx*(e+1)/10
                cy=abs(dx)//beta*(b-8)
                if abs(cy)>min(abs(cx),abs(dx)-abs(cx)):
                    cy=(b-8)/abs(b-8)*min(abs(cx),abs(dx)-abs(cx))
                ls[i]=['q',str(cx),str(cy),str(dx),str(dy)]
        elif ls[i][0] == 'v':
            dx = 0
            dy = eval(ls[i][1])
            if f>8:
                cx1 = (dy // beta) * (a-8)
                cy1 = dy // (3+c)
                if abs(cx1)>abs(cy1):
                    cx1=(a-8)/abs(a-8)*cy1
                cx2=-cx1
                cy2 = dy-cy1
                ls[i] = ['q', str(cx1), str(cy1),str(dx), str(dy//2)]
                ls.insert(i+1,['q', str(cx2),str(cy2-dy//2),str(dx), str(dy-dy//2)])
                i=i+1
            else:
                cx=abs(dy)//beta*(a-8)
                if dy>0:
                    cy=dy*(f+1)/10
                else:
                    cy=dy-dy*(f+1)/10
                if abs(cx)>min(abs(cy),abs(dy)-abs(cy)):
                    cx=min(abs(cy),abs(dy)-abs(cy))*(a-8)/abs(a-8)
                ls[i]=['q',str(cx),str(cy),str(dx),str(dy)]
        elif (ls[i][0] == 'l'):
            dx = eval(ls[i][1])
            dy = eval(ls[i][2])
            cx = dx // 2 + (dx // beta) * a//2
            cy = dy // 2 + (dy // beta) * b//2
            ls[i] = ['q', str(cx), str(cy), str(dx), str(dy)]
        i=i+1
    return ls

def list2xml(ls):
    #是path函数的逆过程，即把List转换为字形信息存储到svg中去
    ret = ""
    for i in ls:
        ret += " ".join(i)
    return ret


def glphyProcessing(s1, s2, ls):
    #给定需要变化的文件位置和变换后文件位置，通过ls（SM3签名预处理得到的List）作为参数进行字形变换
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
    process(old_path, ls[0][partition], ls[1][partition], ls[0][partition2], ls[1][partition2], ls[0][partition3], ls[1][partition3])
    thin(old_path, 1-ls[0][0]/70)
    flat(old_path, 1-ls[1][0]/70)
    tilt(old_path, ls[0][1]/70)
    new = list2xml(old_path)
    tree.getroot()[0].attrib['d'] = new
    tree.write(s2)


def sign2ls(s):
    #把SM3签名转换为List方便字形变换
    n = len(s)
    lsx = []
    lsy = []
    for i in range(int(n / 2)):
        lsx.append(int(s[i], 16))
    for i in range(int(n / 2), n):
        lsy.append(int(s[i], 16))
    return [lsx, lsy]


def allProcessing(sign):
    #对svg文件夹下所有文件调用glphyProcessing进行字符h变换
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
