iptx = [0 for x in range(40)]
ipty = [0 for x in range(40)]
ord_OX=0.0
ord_OY=0.0
ord_XX=0.005
ord_YY=500
pix_OX=0.0
pix_OY=0.0
pix_XX=1.0
pix_XY=0.0
pix_YX=0.0
pix_YY=1.0
A=0.0
accuracy=0
inc0=0
def areatrig(x1,y1,x2,y2,x3,y3):
    return abs(x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3 + x1 * y2 - x2 * y1) / 2
from math import *
import graphics
from graphics import *
from os import system
try:
    win= GraphWin("Interpolator",1300,600)
    win.master.geometry('%dx%d+%d+%d' % (1300,600, 30, 20))
    Myimg=Image(Point(650,300),"pics\\inter_bg.gif")
    Myimg.draw(win)
    Ex0=Entry(Point(1180,180),20)
    Ey0=Entry(Point(1180,210),20)
    Exn=Entry(Point(1180,240),20)
    Eyn=Entry(Point(1180,270),20)
    Ex0.draw(win)
    Ey0.draw(win)
    Exn.draw(win)
    Eyn.draw(win)
    Tpic=Text(Point(1050,100),"Name:")
    Tx0=Text(Point(1060,180),"X0:")
    Ty0=Text(Point(1060,210),"Y0:")
    Txn=Text(Point(1060,240),"Xn:")
    Tyn=Text(Point(1060,270),"Yn:")
    Tpic.draw(win)
    Tx0.draw(win)
    Ty0.draw(win)
    Txn.draw(win)
    Tyn.draw(win)
    Rpic1=Rectangle(Point(1030,125),Point(1140,155))
    Rpic1.draw(win)
    Rpic2=Rectangle(Point(1160,125),Point(1270,155))
    Rpic2.draw(win)
    Top=Text(Point(1085,140),"OpenCurve")
    Top.draw(win)
    Tla=Text(Point(1215,140),"Prev. Data")
    Tla.draw(win)
    Rop1=Rectangle(Point(1060,290),Point(1080,310))
    Rop1.draw(win)
    Rop2=Rectangle(Point(1060,320),Point(1080,340))
    Rop2.draw(win)
    Top1=Text(Point(1142,300),"Include Origin")
    Top1.draw(win)
    Top1=Text(Point(1160,330),"Use High Precision")
    Top1.draw(win)
    Rin=Rectangle(Point(1030,350),Point(1270,380))
    Rin.draw(win)
    Tin=Text(Point(1150,365),"Input Curve")
    Tin.draw(win)
    Exep=Entry(Point(1180,405),20)
    Exep.draw(win)
    Txep=Text(Point(1060,405),"X:")
    Txep.draw(win)
    Efn=Entry(Point(1180,430),20)
    Efn.draw(win)
    Tfn=Text(Point(1050,430),"File name:")
    Tfn.draw(win)
    Rge=Rectangle(Point(1030,455),Point(1270,485))
    Rge.draw(win)
    Tge=Text(Point(1150,470),"Generate Formula")
    Tge.draw(win)
    Rhp=Rectangle(Point(1030,55),Point(1270,85))
    Rhp.draw(win)
    Thp=Text(Point(1150,70),"Help")
    Thp.draw(win)
    Epic=Entry(Point(1180,100),20)
    Epic.draw(win)
    Tinst=Text(Point(500,520),"The picture should have width less than 1000pix and height less than 500pix.")
    Tinst.draw(win)
    while True:
        pt=win.getMouse()
        if(1030<pt.x<1270 and 55<pt.y<85):
            Myimg2=Image(Point(650,300),"pics\\help.gif")
            Myimg2.draw(win)
            win.getMouse()
            Myimg2.undraw()
        if(850<pt.x<930 and 540<pt.y<560):
            system("clip< formula.lin")
            Tinst.move(0,100)
            Tinst=Text(Point(500,520),"Linear function copied to clipbord.")
            Tinst.draw(win)
        if(850<pt.x<930 and 570<pt.y<590):
            system("clip< formula.lan")
            Tinst.move(0,100)
            Tinst=Text(Point(500,520),"Lagrange's function copied to clipbord.")
            Tinst.draw(win)
        if(1030<pt.x<1270 and 455<pt.y<485):
            fil=open("form.txt","w")
            Tinst.move(0,100)
            Tinst=Text(Point(500,520),"The points saved in file:"+"form.txt \n Press any key to exit.")
            Tinst.draw(win)
            for i in range(n):
                fil.write(str(iptx[i])+","+str(ipty[i])+"\n")
            fil.close()
            fprev=open("prev.ax","w")
            fprev.write(Epic.getText()+'\n')
            fprev.write(Ex0.getText()+'\n')
            fprev.write(Ey0.getText()+'\n')
            fprev.write(Exn.getText()+'\n')
            fprev.write(Eyn.getText()+'\n')
            fprev.write(Efn.getText()+'\n')
            fprev.write(Exep.getText()+'\n')
            fprev.close()
            xep=Exep.getText()
            system("data\\inter"+" "+xep+" "+"form.txt"+" "+str(n))
            fil=open("formula.lin","r")
            lines = [line.rstrip('\n') for line in fil]
            Tlin=Text(Point(60,550),"Linear:")
            Tlin.draw(win)
            Elin=Entry(Point(500,550),70)
            Elin.draw(win)
            Elin.setText(lines[0])
            fil.close()
            fil=open("formula.lan","r")
            lines = [line.rstrip('\n') for line in fil]
            Tlan=Text(Point(58,580),"Lagrange's:")
            Tlan.draw(win)
            fil.close()
            Llin=Line(Point(120,559),Point(146,548))
            Llin.setOutline('Red')
            Llin.draw(win)
            Llin=Line(Point(146,548),Point(180,556))
            Llin.setOutline('Red')
            Llin.draw(win)
            Llan=Line(Point(120,589),Point(166,578))
            Llan.setOutline('Blue')
            Llan.draw(win)
            Llan=Line(Point(166,578),Point(180,590))
            Llan.setOutline('Blue')
            Llan.draw(win)
            Elan=Entry(Point(500,580),70)
            Elan.draw(win)
            Elan.setText(lines[0])
            Tlinc=Text(Point(890,550),"Copy")
            Tlinc.draw(win)
            Tlanc=Text(Point(890,580),"Copy")
            Tlanc.draw(win)
            Rlan=Rectangle(Point(850,540),Point(930,560))
            Rlan.draw(win)
            Rlan=Rectangle(Point(850,570),Point(930,590))
            Rlan.draw(win)
            #to plot lagrange's interpolation
            for i in range(n):
                for ip in range(5):
                    x=iptx[i-1]+ip*(iptx[i]-iptx[i-1])/(4)
                    y=0
                    for j in range(n):
                        yp=1
                        for k in range(n):
                            if(k!=j):
                                yp=yp*(x-iptx[k])/(iptx[j]-iptx[k])
                        y=y+yp*ipty[j]
                    x=floor((x-ord_OX)*pix_LX/ord_LX)+pix_OX
                    y=pix_OY-floor((y-ord_OY)*pix_LY/ord_LY)
                    if(i==0):
                        xi=x
                        yi=y
                    else:
                        l=Line(Point(xi,yi),Point(x,y))
                        l.setOutline('Blue')
                        l.draw(win)
                        xi=x
                        yi=y
        if(1030<pt.x<1140 and 125<pt.y<155):
            try:
                img2=Image(Point(500,250),"pics\\"+Epic.getText()+".gif")
                img2.draw(win)
                Tinst.move(0,100)
                Tinst=Text(Point(500,520),"Enter x0,y0,xn,yn.")
                Tinst.draw(win)
            except:
                Tinst.move(0,100)
                Tinst=Text(Point(500,520),"File Not Found. Put the file inside pics folder.")
                Tinst.draw(win)
        if(1160<pt.x<1270 and 125<pt.y<155):
            try:
                fprev=open("prev.ax","r")
                lines = [line.rstrip('\n') for line in fprev]
                Epic.setText(lines[0])
                Ex0.setText(lines[1])
                Ey0.setText(lines[2])
                Exn.setText(lines[3])
                Eyn.setText(lines[4])
                Efn.setText(lines[5])
                Exep.setText(lines[6])
                fprev.close()
                Tinst.move(0,100)
                Tinst=Text(Point(500,520),"x0,y0,xn,yn Read.")
                Tinst.draw(win)
            except:
                Tinst.move(0,100)
                Tinst=Text(Point(500,520),"Previous data not found.")
                Tinst.draw(win)
                Epic.setText('fy_steel')
                Ex0.setText('0')
                Ey0.setText('0')
                Exn.setText('0.005')
                Eyn.setText('500')
                Efn.setText('form')
                Exep.setText('a1')
        if(1060<pt.x<1080 and 290<pt.y<310):
            if(inc0==0):
                inc0=1
                Rop1.setFill('Black')
                Rop1.undraw()
                Rop1.draw(win)
                Tinst.move(0,100)
                Tinst=Text(Point(500,520),"Origin now included in the curve.")
                Tinst.draw(win)
            elif(inc0==1):
                inc0=0
                Rop1.setFill('')
                Rop1.undraw()
                Rop1.draw(win)
                Tinst.move(0,100)
                Tinst=Text(Point(500,520),"Now origin not included in the curve.")
                Tinst.draw(win)
        if(1060<pt.x<1080 and 320<pt.y<340):
            if(accuracy==0):
                accuracy=1
                Rop2.setFill('Black')
                Rop2.undraw()
                Rop2.draw(win)
                Tinst.move(0,100)
                Tinst=Text(Point(500,520),"Multiple clicks needed for single point input.")
                Tinst.draw(win)
            elif(accuracy==1):
                accuracy=0
                Rop2.setFill('')
                Rop2.undraw()
                Rop2.draw(win)
                Tinst.move(0,100)
                Tinst=Text(Point(500,520),"Single click single point input.")
                Tinst.draw(win)
        if(1030<pt.x<1270 and 350<pt.y<380):
            ord_OX=float(Ex0.getText())
            ord_OY=float(Ey0.getText())
            ord_XX=float(Exn.getText())
            ord_YY=float(Eyn.getText())
            #get points for origin, x-extreme and y-extreme
            Tinst.move(0,100)
            Tinst=Text(Point(500,520),"Click at the Origin.")
            Tinst.draw(win)
            pt=win.getMouse()
            pix_OX=pt.x
            pix_OY=pt.y
            inpC=Circle(pt,8)
            inpL1=Line(Point(pt.x,pt.y-4),Point(pt.x,pt.y+4))
            inpL2=Line(Point(pt.x+4,pt.y),Point(pt.x-4,pt.y))
            inpC.setOutline('Red')
            inpL1.setOutline('Red')
            inpL2.setOutline('Red')
            inpL1.draw(win)
            inpL2.draw(win)
            inpC.draw(win)
            k=1
            if accuracy==1:
                while True:
                    inpC.undraw()
                    inpL1.undraw()
                    inpL2.undraw()
                    inpC=Circle(pt,8)
                    inpL1=Line(Point(pt.x,pt.y-4),Point(pt.x,pt.y+4))
                    inpL2=Line(Point(pt.x+4,pt.y),Point(pt.x-4,pt.y))
                    inpC.setOutline('Red')
                    inpL1.setOutline('Red')
                    inpL2.setOutline('Red')
                    inpL1.draw(win)
                    inpL2.draw(win)
                    inpC.draw(win)
                    pt=win.getMouse()
                    if(pt.x>1000 or pt.y>500):
                        break
                    pix_OX=(pix_OX*k+pt.x)/(k+1)
                    pix_OY=(pix_OY*k+pt.y)/(k+1)
                    k=k+1
                    pt.x=pix_OX
                    pt.y=pix_OY
            Tinst.move(0,100)
            Tinst=Text(Point(500,520),"Click at X-axis extreme point.")
            Tinst.draw(win)
            pt=win.getMouse()
            inpC=Circle(pt,8)
            inpL1=Line(Point(pt.x,pt.y-4),Point(pt.x,pt.y+4))
            inpL2=Line(Point(pt.x+4,pt.y),Point(pt.x-4,pt.y))
            inpC.setOutline('Red')
            inpL1.setOutline('Red')
            inpL2.setOutline('Red')
            inpL1.draw(win)
            inpL2.draw(win)
            inpC.draw(win)
            pix_XX=pt.x
            pix_XY=pt.y
            k=1
            if accuracy==1:
                while True:
                    inpC.undraw()
                    inpL1.undraw()
                    inpL2.undraw()
                    inpC=Circle(pt,8)
                    inpL1=Line(Point(pt.x,pt.y-4),Point(pt.x,pt.y+4))
                    inpL2=Line(Point(pt.x+4,pt.y),Point(pt.x-4,pt.y))
                    inpC.setOutline('Red')
                    inpL1.setOutline('Red')
                    inpL2.setOutline('Red')
                    inpL1.draw(win)
                    inpL2.draw(win)
                    inpC.draw(win)
                    pt=win.getMouse()
                    if(pt.x>1000 or pt.y>500):
                        break
                    pix_XX=(pix_XX*k+pt.x)/(k+1)
                    pix_XY=(pix_XY*k+pt.y)/(k+1)
                    k=k+1
                    pt.x=pix_XX
                    pt.y=pix_XY
            Tinst.move(0,100)
            Tinst=Text(Point(500,520),"Click at Y-axis extreme point.")
            Tinst.draw(win)
            pt=win.getMouse()
            inpC=Circle(pt,8)
            inpL1=Line(Point(pt.x,pt.y-4),Point(pt.x,pt.y+4))
            inpL2=Line(Point(pt.x+4,pt.y),Point(pt.x-4,pt.y))
            inpC.setOutline('Red')
            inpL1.setOutline('Red')
            inpL2.setOutline('Red')
            inpL1.draw(win)
            inpL2.draw(win)
            inpC.draw(win)
            pix_YX=pt.x
            pix_YY=pt.y
            k=1
            if accuracy==1:
                while True:
                    inpC.undraw()
                    inpL1.undraw()
                    inpL2.undraw()
                    inpC=Circle(pt,8)
                    inpL1=Line(Point(pt.x,pt.y-4),Point(pt.x,pt.y+4))
                    inpL2=Line(Point(pt.x+4,pt.y),Point(pt.x-4,pt.y))
                    inpC.setOutline('Red')
                    inpL1.setOutline('Red')
                    inpL2.setOutline('Red')
                    inpL1.draw(win)
                    inpL2.draw(win)
                    inpC.draw(win)
                    pt=win.getMouse()
                    if(pt.x>1000 or pt.y>500):
                        break
                    pix_YX=(pix_YX*k+pt.x)/(k+1)
                    pix_YY=(pix_YY*k+pt.y)/(k+1)
                    k=k+1
                    pt.x=pix_YX
                    pt.y=pix_YY
            #accurate input to be written later
            if abs(pix_OY-pix_XY)<(1+(1-accuracy)*5):
                pix_OY=(pix_OY+pix_XY)/2
                pix_XY=pix_OY
            if abs(pix_OX-pix_YX)<(1+(1-accuracy)*5):
                pix_OX=(pix_OX+pix_YX)/2
                pix_YX=pix_OX
            if abs((pix_XX-pix_OX)*(pix_YX-pix_OX)+(pix_XY-pix_OY)*(pix_YY-pix_OY))<(1+(1-accuracy)*5):
                t=1
                theta=(atan((pix_XY-pix_OY)/(pix_XX-pix_OX))-atan((pix_YX-pix_OX)/(pix_YY-pix_OY)))/2
                cosA=cos(theta)
                sinA=sin(theta)
            else:
                t=2
            pix_LX=sqrt(pow((pix_XX-pix_OX),2)+pow((pix_XY-pix_OY),2))
            pix_LY=sqrt(pow((pix_YX-pix_OX),2)+pow((pix_YY-pix_OY),2))
            ord_LX=ord_XX-ord_OX
            ord_LY=ord_YY-ord_OY
            A=areatrig(pix_OX,pix_OY,pix_XX,pix_XY,pix_YX,pix_YY)
            #now to draw the axes
            X_axis=Line(Point(pix_OX-.1*(pix_XX-pix_OX),pix_OY-.1*(pix_XY-pix_OY)),Point(min(pix_XX+.1*(pix_XX-pix_OX),1000),pix_XY+.1*(pix_XY-pix_OY)))
            X_axis.setOutline('Violet')
            X_axis.setWidth(2)
            X_axis.draw(win)
            Y_axis=Line(Point(pix_OX-.1*(pix_YX-pix_OX),min(pix_OY-.1*(pix_YY-pix_OY),500)),Point(pix_YX+.1*(pix_YX-pix_OX),pix_YY+.1*(pix_YY-pix_OY)))
            Y_axis.setOutline('Violet')
            Y_axis.setWidth(2)
            Y_axis.draw(win)
            ftemp=open("ftemp.txt","w")
            ftemp.write(str(pix_OX)+","+str(pix_OY)+"\n")
            ftemp.write(str(pix_XX)+","+str(pix_XY)+"\n")
            ftemp.write(str(pix_YX)+","+str(pix_YY)+"\n")
            ftemp.close()
            #get points for interpolation
            n=0
            if(inc0==1):
                iptx[0]=ord_OX
                ipty[0]=ord_OY
                xi=pix_OX
                yi=pix_OY
                n=1
            Tinst.move(0,100)
            Tinst=Text(Point(500,520),"Click Points following the curve in order. click outside the area to end.")
            Tinst.draw(win)
            while True:
                inpC.undraw()
                inpL1.undraw()
                inpL2.undraw()
                inpC=Circle(pt,8)
                inpL1=Line(Point(pt.x,pt.y-4),Point(pt.x,pt.y+4))
                inpL2=Line(Point(pt.x+4,pt.y),Point(pt.x-4,pt.y))
                inpC.setOutline('Red')
                inpL1.setOutline('Red')
                inpL2.setOutline('Red')
                inpL1.draw(win)
                inpL2.draw(win)
                inpC.draw(win)
                pt=win.getMouse()
                xtemp=pt.x
                ytemp=pt.y
                k=1
                if accuracy==1:
                    while True:
                        inpC.undraw()
                        inpL1.undraw()
                        inpL2.undraw()
                        inpC=Circle(pt,8)
                        inpL1=Line(Point(pt.x,pt.y-4),Point(pt.x,pt.y+4))
                        inpL2=Line(Point(pt.x+4,pt.y),Point(pt.x-4,pt.y))
                        inpC.setOutline('Red')
                        inpL1.setOutline('Red')
                        inpL2.setOutline('Red')
                        inpL1.draw(win)
                        inpL2.draw(win)
                        inpC.draw(win)
                        pt=win.getMouse()
                        if(pt.x>1000 or pt.y>500):
                            inpC.undraw()
                            inpL1.undraw()
                            inpL2.undraw()
                            Tinst.move(0,100)
                            Tinst=Text(Point(500,520),"Point Input finished.Goto Next point.")
                            Tinst.draw(win)
                            pt.x=xtemp
                            pt.y=ytemp
                            break
                        xtemp=(xtemp*k+pt.x)/(k+1)
                        ytemp=(ytemp*k+pt.y)/(k+1)
                        k=k+1
                        pt.x=xtemp
                        pt.y=ytemp
                if(pt.x>1000 or pt.y>500):
                    Tinst.move(0,100)
                    Tinst=Text(Point(500,520),"All Point Input finished.")
                    Tinst.draw(win)
                    inpC.undraw()
                    inpL1.undraw()
                    inpL2.undraw()
                    break
                if t==0:
                    iptx[n]=(pt.x-pix_OX)*ord_LX/pix_LX+ord_OX
                    ipty[n]=(pt.y-pix_OY)*ord_LY/pix_LY+ord_OY
                elif t==1:
                    iptx[n]=((pt.x-pix_OX)*(pix_XX-pix_OX)+(pt.y-pix_OY)*(pix_XY-pix_OY))*ord_LX/pow(pix_LX,2)+ord_OX
                    ipty[n]=((pt.x-pix_OX)*(pix_YX-pix_OX)+(pt.y-pix_OY)*(pix_YY-pix_OY))*ord_LY/pow(pix_LY,2)+ord_OY
                elif t==2:
                    #length=sqrt(pow((pt.x-pix_OX),2)+pow((pt.y-pix_OY),2))
                    #alpha=acos(((pt.x-pix_OX)*(pix_XX-pix_OX)+(pt.y-pix_OY)*(pix_XY-pix_OY))/(length*pix_LX))
                    #beta=acos(((pt.x-pix_OX)*(pix_YX-pix_OX)+(pt.y-pix_OY)*(pix_YY-pix_OY))/(length*pix_LY))
                    #iptx[n]=(length*sin(beta)/sin(alpha+beta))*ord_LX/pix_LX
                    #ipty[n]=(length*sin(alpha)/sin(alpha+beta))*ord_LY/pix_LY
                    a1=areatrig(pt.x,pt.y,pix_XX,pix_XY,pix_YX,pix_YY)
                    a2=areatrig(pix_OX,pix_OY,pt.x,pt.y,pix_YX,pix_YY)
                    a3=areatrig(pix_OX,pix_OY,pix_XX,pix_XY,pt.x,pt.y)
                    iptx[n]=(a1*ord_OX+a2*ord_XX)/A
                    ipty[n]=(a1*ord_OY+a3*ord_YY)/A
                x=pt.x
                y=pt.y
                if(n==0):
                    xi=x
                    yi=y
                else:
                    l=Line(Point(xi,yi),Point(x,y))
                    l.setOutline('Red')
                    l.draw(win)
                    xi=x
                    yi=y
                n=n+1
finally:
    win.close()
