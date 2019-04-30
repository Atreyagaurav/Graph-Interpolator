
#---------------------------------------------------------------------------------------------
#                                             CLASS
#---------------------------------------------------------------------------------------------
class GraphArea:
    def __init__(self,x0,y0,xn,yn,px0,py0,px1,py1,px2,py2):
        #self.Porigin=origin
        #self.Px_axis=x_axis
        #self.Py_axix=y_axis
        #self.Rorigin=ORIGIN
        #self.Rx_axis=X_AXIS
        #self.Ry_axix=Y_AXIS
        global ACCURACY
        global win
        global Instruction
        self.X_axis=Line(Point(px0-.1*(px1-px0),py0-.1*(py1-py0)),Point(min(px1+.1*(px1-px0),1000),py1+.1*(py1-py0)))
        self.X_axis.setOutline('Violet')
        self.X_axis.setWidth(2)
        self.X_axis.draw(win)
        self.Y_axis=Line(Point(px0-.1*(px2-px0),min(py0-.1*(py2-py0),500)),Point(px2+.1*(px2-px0),py2+.1*(py2-py0)))
        self.Y_axis.setOutline('Violet')
        self.Y_axis.setWidth(2)
        self.Y_axis.draw(win)
        Lx=xn-x0
        Ly=yn-y0
        self.Ox=x0
        self.Oy=y0
        self.Lx=Lx
        self.Ly=Ly
        self.l=px0
        self.m=py0
        self.Sxx=Dist(px1,py1,px0,py0)/Lx
        self.Syy=Dist(px2,py2,px0,py0)/Ly
        self.Sxy=0.0
        self.Syx=0.0
        self.p=0.0
        self.q=0.0
        if(fabs(py0-py1)<(1+5*(1-ACCURACY))):
            py1=(py1+py0)/2
            py0=py1
        if(fabs(px0-px2)<(1+5*(1-ACCURACY))):
            px0=(px0+px2)/2
            px2=px0
        if(px0==px2 and py0==py1):
            self.Sxx=(px1-px0)/Lx
            self.Syy=(py2-py0)/Ly
            self.Sxy=0.0
            self.Syx=0.0
            self.p=0.0
            self.q=0.0
            self.InvSxx=1/self.Sxx
            self.InvSxy=0
            self.InvSyx=0
            self.InvSyy=1/self.Syy
            self.Invl=-self.l/self.Sxx
            self.Invm=-self.m/self.Syy
            self.Invp=0
            self.Invq=0
            self.Invz=1
        elif(Dist(px1,py1,px2,py2)-sqrt(Lx*Lx+Ly*Ly)<1+5*(1-ACCURACY)):
            theta=1
            # to be written later
        else:
            Instruction.update("Enter the fourth point at the corner - opposite to the origin.")
            pt=win.getMouse()
            px3=pt.x
            py3=pt.y
            for i in range(10000):
                self.Sxx=(px1*(self.p*Lx+1)-self.l)/Lx;
                self.Syx=(py1*(self.p*Lx+1)-self.m)/Lx;
                self.Sxy=(px2*(self.q*Ly+1)-self.l)/Ly;
                self.Syy=(py2*(self.q*Ly+1)-self.m)/Ly;
                temp1=self.p
                temp2=self.q
                self.p=(self.p+.1*((px3*(self.p*Lx+self.q*Ly+1)-Sxy*Ly)-px1)/(Lx*px1))/1.1;
                self.q=(self.q+.1*((py3*(self.p*Lx+self.q*Ly+1)-Syx*Lx)-py2)/(Ly*py2))/1.1;
                self.err=(temp1-p)*(temp1-p)+(temp2-q)*(temp2-q);
                if ((Sxy==Syx and Sxy==0 and self.err<0.01) or self.err<0.000000000000001):
                    break
            Inv=[[0.0 for i in range(3)] for x in range(3)]
            InvSol=[[0.0 for i in range(3)] for x in range(3)]
            Inv[0][0]=self.Sxx
            Inv[0][1]=self.Syx
            Inv[0][2]=self.p
            Inv[1][0]=self.Sxy
            Inv[1][1]=self.Syy
            Inv[1][2]=self.q
            Inv[2][0]=self.l
            Inv[2][1]=self.m
            Inv[2][2]=1
            for i in range(3):
                InvSol[i][i]=1
            for i in range(3):
                for j in range(3):
                    if(j<i):
                        continue
                    elif(i==j):
                        for k in range(3):
                            Inv[i][k]=Inv[i][k]/Inv[i][i]
                    else:
                        rat=Inv[i][j]/Inv[i][i]
                        for k in range(3):
                            Inv[j][k]=Inv[j][k]-rat*Inv[i][k]
                            InvSol[j][k]=InvSol[j][k]-rat*InvSol[i][k]
            for i in range(3):
                for j in range(3):
                    if(j<(3-i)):
                        rat=Inv[2-i][j]
                        for k in range(3):
                            Inv[j][k]=Inv[j][k]-rat*Inv[2-i][k]
                            InvSol[j][k]=InvSol[j][k]-rat*InvSol[2-i][k]
            self.InvSxx=InvSol[0][0]
            self.InvSxy=InvSol[1][0]
            self.InvSyx=InvSol[0][1]
            self.InvSyy=InvSol[1][1]
            self.Invl=InvSol[2][0]
            self.Invm=InvSol[2][1]
            self.Invp=InvSol[0][2]
            self.Invq=InvSol[1][2]
            self.Invz=InvSol[2][2]
    def realPoint(self,pt):
        rpt=pt
        rpt.x=(self.InvSxx*rpt.x+self.InvSxy*rpt.y+self.Invl)/(self.Invp*rpt.x+self.Invq*pt.y+self.Invz) +self.Ox
        rpt.y=(self.InvSyx*rpt.x+self.InvSyy*rpt.y+self.Invm)/(self.Invp*rpt.x+self.Invq*pt.y+self.Invz) +self.Oy
        return rpt
    def pixelPoint(self,rpt):
        pt=rpt
        rpt.x=rpt.x-self.Ox
        rpt.y=rpt.y-self.Oy
        pt.x=(self.Sxx*rpt.x+self.Sxy*rpt.y+self.l)/(self.p*rpt.x+self.q*pt.y+1)
        pt.y=(self.Syx*rpt.x+self.Syy*rpt.y+self.m)/(self.p*rpt.x+self.q*pt.y+1)
        return pt
    def clearAxes(self):
        self.X_axis.undraw()
        self.Y_axis.undraw()
    def drawAxes(self):
        self.X_axis.draw(win)
        self.Y_axis.draw(win)

class WaterLevel:
    global win
    def __init__(self,Graph,p,h,n,x=[],y=[]):
        self.Hmax=min(y[0],y[n-1])-min(y)
        self.Depth=h
        self.Graph=Graph
        if(self.Hmax<self.Depth):
            self.Depth=self.Hmax
        self.Level=min(y)+self.Depth
        i=leftIndex(self.Level,y)
        self.Xmin=x[i]-(x[i]-x[i-1])*(self.Level-y[i])/(y[i-1]-y[i])
        i=rightIndex(self.Level,y)
        self.Xmax=x[i]-(x[i]-x[i+1])*(self.Level-y[i])/(y[i+1]-y[i])
        self.TopWidth=self.Xmax-self.Xmin
        self.Area=0
        self.Perimeter=0
        self.l=[]
        flagWet=False
        flagWetPrevious=False
        for i in range(n):
            flagWetPrevious=flagWet
            if(y[i]>self.Level):
                flagWet=False
            else:
                flagWet=True
            try:
                if(flagWet and flagWetPrevious):
                    tempArea=(x[i]-x[i-1])*(self.Level*2-y[i]-y[i-1])/2
                    tempPerimeter=Dist(x[i],y[i],x[i-1],y[i-1])
                elif(flagWet and (not flagWetPrevious)):
                    distance_wet=(x[i]-x[i-1])*(self.Level-y[i])/(y[i-1]-y[i])
                    tempArea=.5*distance_wet*(self.Level-y[i])
                    tempPerimeter=Dist(0,self.Level,distance_wet,y[i])
                elif(flagWetPrevious and (not flagWet)):
                    distance_wet=(x[i]-x[i-1])*(self.Level-y[i-1])/(y[i]-y[i-1])
                    tempArea=.5*distance_wet*(self.Level-y[i-1])
                    tempPerimeter=Dist(0,self.Level,distance_wet,y[i-1])
                else:
                    tempArea=0
                    tempPerimeter=0
            except:
                tempArea=0
                tempPerimeter=0
            finally:
                self.Area=self.Area+tempArea
                self.Perimeter=self.Perimeter+tempPerimeter
    def drawLevel(self,col='Blue'):
        global win
        self.l=Line(self.Graph.pixelPoint(Point(self.Xmin,self.Level)),self.Graph.pixelPoint(Point(self.Xmax,self.Level)))
        self.l.setOutline(col)
        self.l.draw(win)
        return self.l
    def deleteLevel(self):
        self.l.undraw()
class EntryBox:
    global win
    def __init__(self,Label,X_ord,Y_ord,Size):
        self.Label=Label
        self.X=X_ord
        self.Y=Y_ord
        self.Size=Size
        self._Entry=Entry(Point(X_ord+Size/2,Y_ord),Size)
        self._Text=Text(Point(X_ord-len(Label)*5-Size*5,Y_ord),Label+" :")
        self._Entry.draw(win)
        self._Text.draw(win)
    def read(self):
        return self._Entry.getText()
    def insert(self,str):
        self._Entry.setText(str)
    def delete(self):
        self._Entry.undraw()
        self._Text.undraw()
class CheckBox:
    global win
    def __init__(self,Label,X_ord,Y_ord):
        self.Label=Label
        self.X=X_ord
        self.Y=Y_ord
        self.Size=V_SIZE
        self.IsTrue=False
        self.IsAvailable=True
        self._Box=Rectangle(Point(X_ord-V_SIZE/2,Y_ord-V_SIZE/2),Point(X_ord+V_SIZE/2,Y_ord+V_SIZE/2))
        self._Text=Text(Point(X_ord+V_SIZE+len(Label)*4,Y_ord),Label)
        self._Box.draw(win)
        self._Text.draw(win)
    def toggle(self):
        if self.IsTrue==False:
            self.IsTrue=True
            self._Box.setFill('Black')
            self.update()
        else:
            self.IsTrue=False
            self._Box.setFill('')
            self.update()
    def check(self):
        self.IsTrue=True
        self._Box.setFill('Black')
        self.update()
    def uncheck(self):
        self.IsTrue=False
        self._Box.setFill('')
        self.update()
    def update(self):
        self._Box.undraw()
        self._Box.draw(win)
        self._Text.setText(self.Label)
    def includes(self,pt):
        if((self.X-self.Size/2)<pt.x<(self.X+self.Size/2) and (self.Y-self.Size/2)<pt.y<(self.Y+self.Size/2)):
            return self.IsAvailable
        else:
            return False
    def available(self):
        self._Box.setOutline('Black')
        self._Text.setTextColor('Black')
        self.IsAvailable=True
        self.update()
    def unavailable(self):
        self._Box.setOutline('Grey')
        self._Text.setTextColor('Grey')
        self.IsAvailable=False
        self.uncheck()
    def delete(self):
        self._Box.undraw()
        self._Text.undraw()
class Button:
    global win
    def __init__(self,Label,X_ord,Y_ord,SizeX,SizeY=26,fancy=0):
        self.Label=Label
        self.X=X_ord
        self.Y=Y_ord
        self.SizeX=SizeX
        self.SizeY=SizeY
        self.IsAvailable=True
        self._Box=Rectangle(Point(X_ord-SizeX/2,Y_ord-SizeY/2),Point(X_ord+SizeX/2,Y_ord+SizeY/2))
        self._Text=Text(Point(X_ord,Y_ord),Label)
        if fancy==1:
            self._Box.setWidth(5)
            self._Box.setOutline('Violet')
            self._Text.setSize(min(20,self.SizeY))
        self._Box.draw(win)
        self._Text.draw(win)
    def includes(self,pt):
        if((self.X-self.SizeX/2)<pt.x<(self.X+self.SizeX/2) and (self.Y-self.SizeY/2)<pt.y<(self.Y+self.SizeY/2)):
            return self.IsAvailable
        else:
            return False
    def update(self):
        self._Box.undraw()
        self._Text.undraw()
        self._Box=Rectangle(Point(self.X-self.SizeX/2,self.Y-self.SizeY/2),Point(self.X+self.SizeX/2,self.Y+self.SizeY/2))
        self._Text=Text(Point(self.X,self.Y),self.Label)
        self._Box.draw(win)
        self._Text.draw(win)
    def available(self):
        self._Box.setOutline('Black')
        self._Text.setTextColor('Black')
        self.update()
        self.IsAvailable=True
    def unavailable(self):
        self._Box.setOutline('Grey')
        self._Text.setTextColor('Grey')
        self.IsAvailable=False
        self.update()
    def delete(self):
        self._Box.undraw()
        self._Text.undraw()
class Writing:
    global win
    def __init__(self,Label,x=500,y=520):
        self.Label=Label
        self.x=x
        self.y=y
        self._Text=Text(Point(self.x,self.y),Label)
        self._Text.draw(win)
    def update(self,Label):
        self.Label=Label
        self._Text.setText(Label)
    def clear(self):
        self.Label=""
        self._Text.setText("")
    def delete(self):
        self._Text.undraw()
class MarkPoint:
    global win
    def __init__(self,pt):
        self.x=pt.x
        self.y=pt.y
        self._L1=Line(Point(pt.x+3,pt.y+3),Point(pt.x-3,pt.y-3))
        self._L2=Line(Point(pt.x+3,pt.y-3),Point(pt.x-3,pt.y+3))
        self._C=Circle(pt,8)
        self._L1.setOutline('Brown')
        self._L2.setOutline('Brown')
        self._C.setOutline('Brown')
        self._L1.draw(win)
        self._L2.draw(win)
        self._C.draw(win)
    def delete(self):
        self._L1.undraw()
        self._L2.undraw()
        self._C.undraw()
    def update(self,pt):
        self._L1.move(pt.x-self.x,pt.y-self.y)
        self._L2.move(pt.x-self.x,pt.y-self.y)
        self._C.move(pt.x-self.x,pt.y-self.y)
        self.x=pt.x
        self.y=pt.y
class TableRow:
    global win
    def __init__(self,x,y,s,*args):
        if y+V_SIZE>500:
            return
        self.Columns=len(args)
        self.Size=s
        self.X=x
        self.Y=y
        self._Box=[]
        self._Text=[]
        for i in range(len(args)):
            self._Box.append(Rectangle(Point(x+s*i,y),Point(x+s+s*i,y+V_SIZE)))
            self._Box[i].setFill('Lime')
            self._Box[i].draw(win)
            self._Text.append(Text(Point(x+self.Size/2+self.Size*i,y+V_SIZE/2),str(args[i])))
            self._Text[i].draw(win)
    def update(self,*args):
        if len(args)==self.Columns:
            for i in range(self.Columns):
                self._Text[i].setText(str(args[i]))
        else:
            for i in range(self.Columns):
                self._Box[i].undraw()
                self._Text[i].undraw()
            self._Box.clear()
            self._Text.clear()
            self.Columns=len(args)
            for i in range(self.Columns):
                self._Box.append(Rectangle(Point(self.X+self.Size*i,self.Y),Point(self.X+self.Size+self.Size*i,self.Y+V_SIZE)))
                self._Box[i].setFill('Lime')
                self._Box[i].draw(win)
                self._Text.append(Text(Point(self.X+self.Size/2+self.Size*i,self.Y+V_SIZE/2),str(args[i])))
                self._Text[i].draw(win)

#---------------------------------------------------------------------------------------------
#                                             FUNCTIONS
#---------------------------------------------------------------------------------------------
def clearScreen(win):
    for obj in win.items[:]:
        obj.undraw()
def areatrig(x1,y1,x2,y2,x3,y3):
    return abs(x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3 + x1 * y2 - x2 * y1) / 2
def plotPoints(Graph,x=[],y=[]):
    global win
    minX=x[0]
    minY=y[0]
    maxX=x[0]
    maxY=y[0]
    nx=0
    for i in x:
        if minX>i:
            minX=i
        if maxX<i:
            maxX=i
        nx=nx+1
    ny=0
    for i in y:
        if minY>i:
            minY=i
        if maxY<i:
            maxY=i
        ny=ny+1
    n=min(nx,ny)
    for i in range(n):
        if i==0:
            continue
        l=Line(Graph.pixelPoint(Point(x[i-1],y[i-1])),Graph.pixelPoint(Point(x[i],y[i])))
        pt=Graph.pixelPoint(Point(x[i],y[i]))
        l.setOutline('Red')
        l.draw(win)
def Drawline(x1,y1,x2,y2,color):
    Llin=Line(Point(x1,y1),Point(x2,y2))
    Llin.setOutline(color)
    Llin.draw(win)
    return Llin
def Dist(x1,y1,x2,y2):
    return math.pow(math.pow(x1-x2,2)+math.pow(y1-y2,2),.5)
def nearest3(xi,yi,n,x=[],y=[],z=[]):
    zi=z[n-1]
    distance=Dist(xi,yi,x[n-1],y[n-1])
    for i in range(n-1):
        if distance>Dist(x[i],y[i],xi,yi):
            distance=Dist(x[i],y[i],xi,yi)
            zi=z[i]
    return zi
def nearest2(xi,n,x=[],y=[]):
    yi=y[n-1]
    distance=math.fabs(xi-x[n-1])
    for i in range(n-1):
        if distance>math.fabs(xi-x[i]):
            distance=math.fabs(xi-x[i])
            yi=y[i]
    return yi
def inversesq3(N,xi,yi,n,x=[],y=[],z=[]):
    if N>n:
        return
    num=0
    denum=0
    rnk=[]
    for i in range(N):
        c=0
        distance=Dist(max(x),max(y),min(x),min(y))
        for j in range(n):
            if j in rnk:
                continue
            if distance>=Dist(xi,yi,x[j],y[j]):
                distance=Dist(xi,yi,x[j],y[j])
                c=j
        rnk.append(c)
        try:
            num=num+z[c]/(distance*distance)
            denum=denum+1/(distance*distance)
        except(ZeroDivisionError):
            return z[c]
    return num/denum
def inversesq2(N,xi,n,x=[],y=[]):
    if N>n:
        return
    num=0
    denum=0
    rnk=[]
    for i in range(N):
        c=0
        distance=math.pow(max(x)-min(x),2)
        for j in range(n):
            if j in rnk:
                continue
            if distance>=math.pow(xi-x[j],2):
                distance=math.pow(xi-x[j],2)
                c=j
        rnk.append(c)
        try:
            num=num+y[c]/(distance)
            denum=denum+1/(distance)
        except(ZeroDivisionError):
            return y[c]
    return num/denum
def linear2(xi,n,x=[],y=[]):
    yless=min(y)
    ymore=max(y)
    dless=xi-min(x)
    dmore=max(x)-xi
    for i in range(n):
        if (x[i]>xi and dmore>=math.fabs(x[i]-xi)):
            dmore=math.fabs(x[i]-xi)
            ymore=y[i]
        if (x[i]<xi and dless>=math.fabs(x[i]-xi)):
            dless=math.fabs(x[i]-xi)
            yless=y[i]
        if((dless+dmore)==0):
            return (yless+ymore)/2
    if (xi<(.9*min(x)) or xi>(1.1*max(x))):
        return
    else:
        return (dless*ymore+dmore*yless)/(dless+dmore)

def lagrange2(xi,n,x=[],y=[]):
    sum=0
    for i in range(n):
        mul=1
        for j in range(n):
            if j!=i:
                mul=mul*(xi-x[j])/(x[i]-x[j])
        sum=sum+mul*y[i]
    return sum
def lagrange3(xi,yi,n,x=[],y=[],z=[]):
    sum=0
    for i in range(n):
        mul=1
        for j in range(n):
            if j==i:
                continue
            mul=mul*(xi-x[j])/(x[i]-x[j])*(yi-y[j])/(y[i]-y[j])
        sum=sum+mul*z[i]
    return sum
def trendsurf(N,xi,yi,n,x=[],y=[],z=[]):
    Cn=(N+1)*(N+2)/2

def processIMG(str):
    path=str.rsplit("\\")
    if len(path)==1:
        str="pics\\"+str
    names=path[-1].rsplit(".")
    if len(names)>1:
        names.pop()
    name='.'.join(names)
    system("magick "+str+" -resize 1000x500 pics\\"+name+".gif")
    return "pics\\"+name+".gif"
def processFILE(str,mod="r"):
    path=str.rsplit("\\")
    if len(path)==1:
        str="data\\"+str
    else:
        system("copy "+str+" data /y")
    names=path[-1].rsplit(".")
    path.pop()
    pathC="\\".join(path)+"\\"
    if len(names)>1:
        ext=names[-1]
        names.pop()
    else:
        ext="3dd"
    name='.'.join(names)
    if ext!="3dd":
        system("rename "+"data\\"+name+"."+ext+" "+name+".3dd")
    if mod=="r":
        return "data\\"+name+".3dd"
    if mod=="c":
        return pathC+name+".csv"
    else:
        return pathC+name+"_new."+ext
def lowIndex(xi,x=[]):
    for i in range(len/(x)):
        if(x[i]>xi):
            return(i-1)
    return i
def highIndex(xi,x=[]):
    for i in range(len(x)):
        if(x[i]>xi):
            return i
    return i
def leftIndex(yi,y=[]):
    n=len(y)
    i=0
    while True:
        if(y[i]<yi):
            return i
        elif(i>=n):
            return n
        i=i+1
def rightIndex(yi,y=[]):
    n=len(y)
    i=n-1
    while True:
        if(y[i]<yi):
            return i
        elif(i<=0):
            return 0
        i=i-1
from graphics import*
import math
from math import*
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import numpy
import cv2
from os import system
win= GraphWin("Interpolator",1300,600)
win.master.geometry('%dx%d+%d+%d' % (1300,600, 30, 10))
V_SIZE=20
V_SPACING=30
TABLE_MAX=23
ACCURACY=0
ANALYSIS_PRECISION=.01