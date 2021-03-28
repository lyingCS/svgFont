#conding=utf8
from myConfig import *
from myUtils import *
import xml.etree.ElementTree as ET
import os
import math

def unbeautifySmooth(ls):
	#TODO rename
    j = 0 
    for i in range(len(ls)):
        if ls[j][0] == 'l':
            ls.pop(j)
        else:
            j += 1
    return ls

def prolong(ls,a,uni):
    if uni<3406:
        return ls
    for i in range(len(ls)-1):
        if ls[i][0]=='q' and ls[i+1][0]=='q':
            dx1=eval(ls[i][3])
            dy1=eval(ls[i][4])
            dx2=eval(ls[i+1][3])
            dy2=eval(ls[i+1][4])
            if dx1>0 and dy1>0 and dx2<0 and dy2>0:
                ddx1=a*dx1/16
                dx1=dx1+ddx1
                dx2=dx2-ddx1
                ls[i][3]=str(dx1)
                ls[i+1][3]=str(dx2)
    return ls

def Smooth(ls):
    i=0
    while i<len(ls)-1:
        if ls[i][0]=='q' and ls[i+1][0]=='q':
            dx1=eval(ls[i][3])
            dy1=eval(ls[i][4])
            dx2=eval(ls[i+1][3])
            dy2=eval(ls[i+1][4])
            if dx1<=0 and dx2>=0 and dy1>=0 and dy2<=0:
                ang1=math.atan2(dy1,-dx1)
                ang2=math.atan2(-dy2,dx2)
                if(ang1>ang2):
                    ldx=dx2//gama
                    ldy=dy1//gama
                    ls[i][4]=str(dy1-ldy)
                    ls[i+1][3]=str(dx2-ldx)
                    ls.insert(i+1,['l',str(ldx),str(ldy)])
                elif(ang1<ang2):
                    ldx=(-dx1)//gama
                    ldy=(-dy2)//gama
                    ls[i][3]=str(ldx+dx1)
                    ls[i+1][4]=str(dy2+ldy)
                    ls.insert(i+1,['l',str(-ldx),str(-ldy)])
            elif dx1>=0 and dx2<=0 and dy1>=0 and dy2<=0:
                ang1=math.atan2(dy1,-dx1)
                ang2=math.atan2(-dy2,dx2)
                if(ang1>ang2):
                    ldx=dx1//gama
                    ldy=(-dy2)//gama
                    ls[i][3]=str(-ldx+dx1)
                    ls[i+1][4]=str(ldy+dy2)
                    ls.insert(i+1,['l',str(ldx),str(-ldy)])
                elif(ang1<ang2):
                    ldx=(-dx2)//gama
                    ldy=(dy1)//gama
                    ls[i][4]=str(dy1-ldy)
                    ls[i+1][3]=str(dx2+ldx)
                    ls.insert(i+1,['l',str(-ldx),str(ldy)])
            elif dx1>=0 and dy1<=0 and dx2<=0 and dy2>=0:
                ang1=math.atan2(-dy1,dx1)
                ang2=math.atan2(dy2,-dx2)
                if(ang1>ang2):
                    ldx=(-dx2)//gama
                    ldy=dy1//gama
                    ls[i][4]=str(ldy+dy1)
                    ls[i+1][3]=str(ldx+dx2)
                    ls.insert(i+1,['l',str(-ldx),str(-ldy)])
                elif(ang1<ang2):
                    ldx=dx1//gama
                    ldy=dy2//gama
                    ls[i][3]=str(dx1-ldx)
                    ls[i+1][4]=str(dy2-ldy)
                    ls.insert(i+1,['l',str(ldx),str(ldy)])
            elif dx1<=0 and dy1<=0 and dx2>=0 and dy2>=0:
                ang1=math.atan2(-dy1,-dx1)
                ang2=math.atan2(dy2,dx2)
                if(ang1>ang2):
                    ldx=(dx2)//gama
                    ldy=(-dy1)//gama
                    ls[i][4]=str(dy1+ldy)
                    ls[i+1][3]=str(dx2-ldx)
                    ls.insert(i+1,['l',str(ldx),str(-ldy)])
                elif(ang1<ang2):
                    ldx=(-dx1)//gama
                    ldy=dy2//gama
                    ls[i][3]=str(dx1+ldx)
                    ls[i+1][4]=str(dy2-ldy)
                    ls.insert(i+1,['l',str(-ldx),str(ldy)])
        i+=1
    return ls

def tilt(ls, a):
    for i in range(len(ls)):
        if ls[i][0] == 'q':
            ddx = eval(ls[i][1])-eval(ls[i][2])*a
            dx = eval(ls[i][3])-eval(ls[i][4])*a
            ls[i][1] = str(ddx)
            ls[i][3] = str(dx)
        elif ls[i][0]=='M' or ls[i][0]=='t':
            dx=eval(ls[i][1])-eval(ls[i][2])*a
            ls[i][1]=str(dx)
        elif ls[i][0]=='c':
            cx1=eval(ls[i][1])-eval(ls[i][2])*a
            cx2=eval(ls[i][3])-eval(ls[i][4])*a
            dx=eval(ls[i][5])-eval(ls[i][6])*a
            ls[i][1]=str(cx1)
            ls[i][3]=str(cx2)
            ls[i][5]=str(dx)
    return ls

def thin(ls,a):
    for i in range(len(ls)):
        if ls[i][0] == 'q':
            ddx = eval(ls[i][1])*a
            dx = eval(ls[i][3])*a
            ls[i][1] = str(ddx)
            ls[i][3] = str(dx)
        elif ls[i][0]=='M' or ls[i][0]=='t':
            dx=eval(ls[i][1])*a
            ls[i][1]=str(dx)
        elif ls[i][0]=='c':
            cx1=eval(ls[i][1])*a
            cx2=eval(ls[i][3])*a
            dx=eval(ls[i][5])*a
            ls[i][1]=str(cx1)
            ls[i][3]=str(cx2)
            ls[i][5]=str(dx)
    return ls

def flat(ls,a):
    for i in range(len(ls)):
        if ls[i][0] == 'q':
            ddy = eval(ls[i][2])*a
            dy = eval(ls[i][4])*a
            ls[i][2] = str(ddy)
            ls[i][4] = str(dy)
        elif ls[i][0]=='M' or ls[i][0]=='t':
            dy=eval(ls[i][2])*a
            ls[i][2]=str(dy)
        elif ls[i][0]=='c':
            cy1=eval(ls[i][2])*a
            cy2=eval(ls[i][4])*a
            dy=eval(ls[i][6])*a
            ls[i][2]=str(cy1)
            ls[i][4]=str(cy2)
            ls[i][6]=str(dy)
    return ls
