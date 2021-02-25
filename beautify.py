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

def beautifySmooth(ls):
    i=0
    while i<len(ls)-1:
#         print(i)
        if ls[i][0]=='q' and ls[i+1][0]=='q':
            dx1=int(ls[i][3])
            dy1=int(ls[i][4])
            dx2=int(ls[i+1][3])
            dy2=int(ls[i+1][4])
#             print(dx1,dy1,dx2,dy2)
            if dx1<=0 and dx2>=0 and dy1>=0 and dy2<=0:
                ang1=math.atan2(dy1,-dx1)
                ang2=math.atan2(-dy2,dx2)
#                 print(ang1,ang2)
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
#                 print(ang1,ang2)
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
#                 print(ang1,ang2)
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
#                 print(ang1,ang2)
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