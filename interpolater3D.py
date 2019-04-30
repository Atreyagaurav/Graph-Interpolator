

from classes import*
from rating import*
def InterFromIMG():
    global win
    iptx = []
    ipty = []
    iptz = []
    ord_OX=0.0
    ord_OY=0.0
    ord_XX=1.0
    ord_YY=1.0
    pix_OX=0.0
    pix_OY=0.0
    pix_XX=1.0
    pix_XY=0.0
    pix_YX=0.0
    pix_YY=1.0
    ord_CZ=0.0
    CurveFin=False
    clearScreen(win)
    Myimg=Image(Point(650,300),"pics\\fromimg.gif")
    Myimg.draw(win)
    pt=win.getMouse()
    Myimg.undraw()
    Myimg=Image(Point(650,300),"pics\\inter_bg1.gif")
    Myimg.draw(win)
    Instruction=Writing("Welcome to Graph-Interpolator")
    Back=Button("Back",40,520,75)
    Rating=Button("Rating Curve",940,520,100)
    Pic_name=EntryBox("Name",1180,V_SPACING*1,20)
    Open_curve=Button("Open Curve",1090,V_SPACING*2,130)
    Prev_data=Button("Previous Data",1230,V_SPACING*2,130)
    X0=EntryBox("X0",1180,V_SPACING*3,20)
    Y0=EntryBox("Y0",1180,V_SPACING*4,20)
    Xn=EntryBox("Xn",1180,V_SPACING*5,20)
    Yn=EntryBox("Yn",1180,V_SPACING*6,20)
    TwoD=CheckBox(" 2D Curve ",1080,V_SPACING*7)
    ThreeD=CheckBox(" 3D Curve ",1080,V_SPACING*8)
    IncOrigin=CheckBox("Include Origin",1080,V_SPACING*9)
    HiPrecision=CheckBox("High Precision ",1080,V_SPACING*10)
    Input_curve=Button("Input Curve",1150,V_SPACING*11,250)
    Text(Point(1230,V_SPACING*12),"Variable Names").draw(win)
    Z_current=EntryBox("Z value",1100,350+V_SPACING*.5,5)
    X_symbol=EntryBox("X",1230,V_SPACING*13,10)
    Y_symbol=EntryBox("Y",1230,V_SPACING*14,10)
    Z_symbol=EntryBox("Z",1230,V_SPACING*15,10)
    Text(Point(1150,V_SPACING*16),"Interpolate for").draw(win)
    X_inter=CheckBox("X",1040,V_SPACING*17)
    Y_inter=CheckBox("Y",1140,V_SPACING*17)
    Z_inter=CheckBox("Z",1240,V_SPACING*17)
    F_name=EntryBox("File Name",1180,V_SPACING*18,16)
    Generate=Button("Generate Formula",1150,V_SPACING*19,250)
    Submit=Button("Submit",1080,350+V_SPACING*1.5,110)
    Cancel=Button("Cancel",1080,350+V_SPACING*2.5,110)
    Help=Button("Help",1080,350+V_SPACING*3.5,110)
    Linear=EntryBox("Linear",500,550,80)
    Lagrange=EntryBox("Lagrange",500,580,80)
    Drawline(120,534,146,548,'red')
    Drawline(146,548,166,538,'red')
    Drawline(120,569,136,584,'blue')
    Drawline(136,584,166,570,'blue')
    LinCopy=Button("Copy",950,550,70)
    LanCopy=Button("Copy",950,580,70)
    while True:
        pt=win.getMouse()
        if Back.includes(pt):
            return
        elif Rating.includes(pt):
            RatingFromFILE()
            return
        if Open_curve.includes(pt):
            Pic_name.insert(processIMG(Pic_name.read()))
            if Pic_name.read()=="":
                Instruction.update("Type a file name before opening")
            else:
                try:
                    Curve=Image(Point(500,250),Pic_name.read())
                    Curve.draw(win)
                except:
                    Curve.draw(win)
                    Instruction.update("File not found. Save your file in pics folder in .gif format.")
        elif Help.includes(pt):
            Help_pic=Image(Point(650,300),"pics\\fromimg.gif")
            Help_pic.draw(win)
            win.getMouse()
            Help_pic.undraw()
        elif TwoD.includes(pt):
            TwoD.check()
            ThreeD.uncheck()
            Z_inter.unavailable()
        elif ThreeD.includes(pt):
            ThreeD.check()
            TwoD.uncheck()
            Z_inter.available()
        elif IncOrigin.includes(pt):
            IncOrigin.toggle()
            if IncOrigin.IsTrue==True:
                Instruction.update("Origin now included in the curve.")
            else:
                Instruction.update("Origin now excluded in the curve.")
        elif HiPrecision.includes(pt):
            HiPrecision.toggle()
            if HiPrecision.IsTrue==True:
                Instruction.update("Multiple clicks are used for single point input.")
            else:
                Instruction.update("Single click used for single point input.")
        elif X_inter.includes(pt):
            X_inter.check()
            Y_inter.uncheck()
            Z_inter.uncheck()
        elif Y_inter.includes(pt):
            X_inter.uncheck()
            Y_inter.check()
            Z_inter.uncheck()
        elif Z_inter.includes(pt):
            if(ThreeD.IsTrue==True):
                X_inter.uncheck()
                Y_inter.uncheck()
                Z_inter.check()
            else:
                Instruction.update("Z can't be evaluated in 2D curve.")
        elif Prev_data.includes(pt):
            try:
                fprev=open("data\\"+"prev.ax","r")
                lines = [line.rstrip('\n') for line in fprev]
                Pic_name.insert(lines[0])
                X0.insert(lines[1])
                Y0.insert(lines[2])
                Xn.insert(lines[3])
                Yn.insert(lines[4])
                X_symbol.insert(lines[5])
                Y_symbol.insert(lines[6])
                Z_symbol.insert(lines[7])
                F_name.insert(lines[8])
            except:
                Instruction.update("Previous data not found.")
        elif Generate.includes(pt):
            fdata=open("data\\"+"prev.ax","w")
            fdata.write(Pic_name.read()+'\n')
            fdata.write(X0.read()+'\n')
            fdata.write(Y0.read()+'\n')
            fdata.write(Xn.read()+'\n')
            fdata.write(Yn.read()+'\n')
            fdata.write(X_symbol.read()+'\n')
            fdata.write(Y_symbol.read()+'\n')
            fdata.write(Z_symbol.read()+'\n')
            fdata.write(F_name.read()+'\n')
            fdata.write(str(ord_OX)+'\n')
            fdata.write(str(ord_OY)+'\n')
            fdata.write(str(ord_XX)+'\n')
            fdata.write(str(ord_YY)+'\n')
            fdata.write(str(pix_OX)+'\n')
            fdata.write(str(pix_OY)+'\n')
            fdata.write(str(pix_XX)+'\n')
            fdata.write(str(pix_XY)+'\n')
            fdata.write(str(pix_YX)+'\n')
            fdata.write(str(pix_YY)+'\n')
            fdata.close()
            xep="a1"
            if TwoD.IsTrue==True:
                f3d=open("data\\"+F_name.read()+".3dd","w")
                try:
                    if Y_inter.IsTrue==True:
                        xep=X_symbol.read()
                        for i in range(n):
                            f3d.write(str(iptx[i])+","+str(ipty[i])+'\n')
                        f3d.close()
                    elif X_inter.IsTrue==True:
                        xep=Y_symbol.read()
                        for i in range(n):
                            f3d.write(str(ipty[i])+","+str(iptx[i])+'\n')
                        f3d.close()
                    else:
                        f3d.close()
                    print(str(n))
                    system("inter "+xep+" data\\"+F_name.read()+".3dd "+str(n))
                    fil=open("data\\"+"formula.lin","r")
                    lines = [line.rstrip('\n') for line in fil]
                    Linear.insert(lines[0])
                    fil.close()
                    fil=open("data\\"+"formula.lan","r")
                    lines = [line.rstrip('\n') for line in fil]
                    Lagrange.insert(lines[0])
                    fil.close()
                    #-----------------------------------------------
                    #            to plot lagrange's function
                    #-----------------------------------------------
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
                            #x=floor((x-ord_OX)*pix_LX/ord_LX)+pix_OX
                            #y=pix_OY-floor((y-ord_OY)*pix_LY/ord_LY)
                            lpt=ThisGraph.pixelPoint(Point(x,y))
                            x=lpt.x
                            y=lpt.y
                            if(i==0):
                                xi=x
                                yi=y
                            else:
                                l=Line(Point(xi,yi),Point(x,y))
                                l.setOutline('Blue')
                                l.setWidth(2)
                                l.draw(win)
                                xi=x
                                yi=y
                except:
                    Instruction.update("Write expression for independent variable")
            elif ThreeD.IsTrue==True:
                f3d=open("data\\"+F_name.read()+".3dd","w")
                try:
                    if Z_inter.IsTrue==True:
                        for i in range(n):
                            f3d.write(str(iptx[i])+","+str(ipty[i])+","+str(iptz[i])+'\n')
                        f3d.close()
                    elif Y_inter.IsTrue==True:
                        for i in range(n):
                            f3d.write(str(iptz[i])+","+str(iptx[i])+","+str(ipty[i])+'\n')
                        f3d.close()
                    elif X_inter.IsTrue==True:
                        for i in range(n):
                            f3d.write(str(iptz[i])+","+str(ipty[i])+","+str(iptx[i])+'\n')
                        f3d.close()
                    Instruction.update("The data saved in a file. Go back and open the file to interpolate.")
                except:
                    Instruction.update("write expressions for independent variables.")
        elif LinCopy.includes(pt):
            system("clip< data\\formula.lin")
            Instruction.update("Linear interpolation formula copied to clipboard.")
        elif LanCopy.includes(pt):
            system("clip< data\\formula.lan")
            Instruction.update("Lagrange's interpolation formula copied to clipboard.")
        elif Input_curve.includes(pt):
            #----------------------------------------------------------
            #get reference points for origin, x-extreme and y-extreme
            #----------------------------------------------------------
            ord_OX=float(X0.read())
            ord_OY=float(Y0.read())
            ord_XX=float(Xn.read())
            ord_YY=float(Yn.read())
            Instruction.update("Click at the Origin.")
            pt=win.getMouse()
            pix_OX=pt.x
            pix_OY=pt.y
            M_00=MarkPoint(pt)
            k=1
            while HiPrecision.IsTrue:
                Instruction.update("Click at more points to increase the accuracy. click Submit when done.")
                pt=win.getMouse()
                if Submit.includes(pt):
                    break
                elif (pt.x>1000 or pt.y>500):
                    Instruction.update("Click inside the graph area.")
                else:
                    pix_OX=(pix_OX*k+pt.x)/(k+1)
                    pix_OY=(pix_OY*k+pt.y)/(k+1)
                    pt.x=pix_OX
                    pt.y=pix_OY
                    M_00.update(pt)
                    k=k+1
            Instruction.update("Click at the X-axis extreme point.")
            pt=win.getMouse()
            pix_XX=pt.x
            pix_XY=pt.y
            M_xn=MarkPoint(pt)
            k=1
            while HiPrecision.IsTrue:
                Instruction.update("Click at more points to increase the accuracy. click Submit when done.")
                pt=win.getMouse()
                if Submit.includes(pt):
                    break
                elif (pt.x>1000 or pt.y>500):
                    Instruction.update("Click inside the graph area.")
                else:
                    pix_XX=(pix_XX*k+pt.x)/(k+1)
                    pix_XY=(pix_XY*k+pt.y)/(k+1)
                    pt.x=pix_XX
                    pt.y=pix_XY
                    M_xn.update(pt)
                    k=k+1
            Instruction.update("Click at the Y-axis extreme point.")
            pt=win.getMouse()
            pix_YX=pt.x
            pix_YY=pt.y
            M_yn=MarkPoint(pt)
            k=1
            while HiPrecision.IsTrue:
                Instruction.update("Click at more points to increase the accuracy. click Submit when done.")
                pt=win.getMouse()
                if Submit.includes(pt):
                    break
                elif (pt.x>1000 or pt.y>500):
                    Instruction.update("Click inside the graph area.")
                else:
                    pix_YX=(pix_YX*k+pt.x)/(k+1)
                    pix_YY=(pix_YY*k+pt.y)/(k+1)
                    pt.x=pix_YX
                    pt.y=pix_YY
                    M_yn.update(pt)
                    k=k+1
            #axis input finished
            if HiPrecision==False:
                accuracy=0
            else:
                accuracy=1
            #if abs(pix_OY-pix_XY)<(1+(1-accuracy)*4):
            #    pix_OY=(pix_OY+pix_XY)/2
            #    pix_XY=pix_OY
            #if abs(pix_OX-pix_YX)<(1+(1-accuracy)*4):
            #    pix_OX=(pix_OX+pix_YX)/2
            #    pix_YX=pix_OX
            #if abs((pix_XX-pix_OX)*(pix_YX-pix_OX)+(pix_XY-pix_OY)*(pix_YY-pix_OY))<(1+(1-accuracy)*5):
            #    t=1
            #    theta=(atan((pix_XY-pix_OY)/(pix_XX-pix_OX))-atan((pix_YX-pix_OX)/(pix_YY-pix_OY)))/2
            #    cosA=cos(theta)
            #    sinA=sin(theta)
            #else:
            #    t=2
            ThisGraph=GraphArea(ord_OX,ord_OY,ord_XX,ord_YY,pix_OX,pix_OY,pix_XX,pix_XY,pix_YX,pix_YY)
            pix_LX=sqrt(pow((pix_XX-pix_OX),2)+pow((pix_XY-pix_OY),2))
            pix_LY=sqrt(pow((pix_YX-pix_OX),2)+pow((pix_YY-pix_OY),2))
            ord_LX=ord_XX-ord_OX
            ord_LY=ord_YY-ord_OY
            A=areatrig(pix_OX,pix_OY,pix_XX,pix_XY,pix_YX,pix_YY)
            #now to draw the axes
            M_00.delete()
            M_xn.delete()
            M_yn.delete()
            n=0
            if IncOrigin.IsTrue==True:
                iptx.append(ord_OX)
                ipty.append(ord_OY)
                xi=pix_OX
                yi=pix_OY
                if ThreeD.IsTrue==True:
                    iptz[0]=float(Z_current.read())
                n=1
                #------------------------------------------------------------------------
                #                           POINT INPUT FOR CURVE
                #------------------------------------------------------------------------
            Instruction.update("Clicks the points in the curve in a order.")
            while True:
                pt=win.getMouse()
                if Submit.includes(pt):
                    if TwoD.IsTrue==True:
                        Instruction.update("Points input finished.")
                        break
                    elif ThreeD.IsTrue==True:
                        if CurveFin==False:
                            Instruction.update("Enter New value of Z for the next curve OR Submit again to finish.")
                            CurveFin=True
                        else:
                            Instruction.update("Points input finished for all curves")
                            break
                elif (pt.x>1000 or pt.y>500):
                    Instruction.update("Click inside the graph area.")
                    continue
                else:
                    xtemp=pt.x
                    ytemp=pt.y
                    M_point=MarkPoint(pt)
                    k=1
                    while HiPrecision.IsTrue:
                        Instruction.update("Click at more points to increase the accuracy. click Submit when done.")
                        pt=win.getMouse()
                        if Submit.includes(pt):
                            pt.x=xtemp
                            pt.y=ytemp
                            break
                        elif(pt.x>1000 or pt.y>500):
                            Instruction.update("Click inside the graph area.")
                        else:
                            xtemp=(xtemp*k+pt.x)/(k+1)
                            ytemp=(ytemp*k+pt.y)/(k+1)
                            pt.x=xtemp
                            pt.y=ytemp
                            M_point.update(pt)
                            k=k+1
                    M_point.delete()
                    rpt=ThisGraph.realPoint(pt)
                    iptx.append(rpt.x)
                    ipty.append(rpt.y)
                    #if t==0:
                    #    iptx.append((pt.x-pix_OX)*ord_LX/pix_LX+ord_OX)
                    #    ipty.append((pt.y-pix_OY)*ord_LY/pix_LY+ord_OY)
                    #elif t==1:
                    #    iptx.append(((pt.x-pix_OX)*(pix_XX-pix_OX)+(pt.y-pix_OY)*(pix_XY-pix_OY))*ord_LX/pow(pix_LX,2)+ord_OX)
                    #    ipty.append(((pt.x-pix_OX)*(pix_YX-pix_OX)+(pt.y-pix_OY)*(pix_YY-pix_OY))*ord_LY/pow(pix_LY,2)+ord_OY)
                    #elif t==2:
                    #    a1=areatrig(pt.x,pt.y,pix_XX,pix_XY,pix_YX,pix_YY)
                    #    a2=areatrig(pix_OX,pix_OY,pt.x,pt.y,pix_YX,pix_YY)
                    #    a3=areatrig(pix_OX,pix_OY,pix_XX,pix_XY,pt.x,pt.y)
                    #    iptx.append((a1*ord_OX+a2*ord_XX)/A)
                    #    ipty.append((a1*ord_OY+a3*ord_YY)/A)
                    if ThreeD.IsTrue==True:
                        iptz.append(float(Z_current.read()))
                    if (n==0 or CurveFin==True):
                        xi=xtemp
                        yi=ytemp
                        CurveFin=False
                        Instruction.update("Clicks the points in the curve in a order.")
                    else:
                        Drawline(xi,yi,xtemp,ytemp,'Red')
                        xi=xtemp
                        yi=ytemp
                    n=n+1
#InterFromIMG()
