

from classes import*
def InterFromFILE():
    global win
    clearScreen(win)
    Myimg=Image(Point(650,300),"pics\\fromfile.gif")
    Myimg.draw(win)
    pt=win.getMouse()
    Myimg.undraw()
    Myimg=Image(Point(650,300),"pics\\inter_bg.gif")
    Myimg.draw(win)
    x=[]
    y=[]
    z=[]
    x_c=[]
    y_c=[]
    z_c=[]
    Instruction=Writing("Welcome to Graph-Interpolator")
    Back=Button("Back",40,520,75)
    Pic_name=EntryBox("Pic Name",1200,V_SPACING*1,15)
    Open_curve=Button("Open Pic",1090,V_SPACING*2,130)
    Prev_data=Button("Previous Data",1230,V_SPACING*2,130)
    F_name=EntryBox("File Name",1200,V_SPACING*3,15)
    TwoD=CheckBox("2D",1050,V_SPACING*4)
    ThreeD=CheckBox("3D",1150,V_SPACING*4)
    Open_file=Button("Load",1250,V_SPACING*4,80)
    Plot=Button("Plot Curves",1090,V_SPACING*5,130)
    X_val=EntryBox("X",1100,V_SPACING*6,15)
    Y_val=EntryBox("Y",1100,V_SPACING*7,15)
    Z_val=EntryBox("Z",1100,V_SPACING*8,15)
    X_cal=Button("Calculate",1240,V_SPACING*6,90)
    Y_cal=Button("Calculate",1240,V_SPACING*7,90)
    Z_cal=Button("Calculate",1240,V_SPACING*8,90)
    F_csv=EntryBox("CSV FileName",1200,V_SPACING*9,15)
    Open_csv=Button("Load",1250,V_SPACING*10,80)
    Text(Point(1100,V_SPACING*10),"Interpolation method").draw(win)
    I_lin=CheckBox("Linear ",1050,V_SPACING*11)
    I_lan=CheckBox(" Lagrange",1050,V_SPACING*12)
    I_near=CheckBox("Nearest Neighbour",1050,V_SPACING*13)
    I_invsq=CheckBox("Inverse Square",1050,V_SPACING*14)
    I_trend=CheckBox("Trend ",1050,V_SPACING*15)
    N_invsq=EntryBox("   N",1260,V_SPACING*14,3)
    N_trend=EntryBox("   n",1260,V_SPACING*15,3)
    InterpolateZ=Button("Interpolate",1090,V_SPACING*16,130)
    Save_csv=Button("Save",1230,V_SPACING*16,130)
    Linear=EntryBox("Linear",500,550,80)
    Lagrange=EntryBox("Lagrange",500,580,80)
    Drawline(120,534,146,548,'red')
    Drawline(146,548,166,538,'red')
    Drawline(120,569,136,584,'blue')
    Drawline(136,584,166,570,'blue')
    LinCopy=Button("Copy",950,550,70)
    LanCopy=Button("Copy",950,580,70)
    ThreeD.check()
    I_lan.check()
    I_lin.unavailable()
    I_trend.unavailable()
    while True:
        pt=win.getMouse()
        if Back.includes(pt):
            return
        if Plot.includes(pt):
            if TwoD.IsTrue:
                try:
                    ThisGraph.drawAxes()
                    ThisGraph.plotPoints(x,y)
                except:
                    ThisGraph=GraphArea(min(x),min(y),max(x),max(y),200,450,800,450,200,50)
                    plotPoints(ThisGraph,x,y)
            elif ThreeD.IsTrue:
                #ar3d=numpy.array([x,y,z])
                fig = plt.figure()
                ax = fig.add_subplot(1, 2, 1, projection='3d')
                ax.scatter(x,y,z)#ar3d[:,0],ar3d[:,1],ar3d[:,2])
                fig.show()
        if Open_curve.includes(pt):
            Pic_name.insert(processIMG(Pic_name.read()))
            if Pic_name.read()=="":
                Instruction.update("Type a file name before opening")
            else:
                try:
                    Curve=Image(Point(500,250),processIMG(Pic_name.read()))
                    Curve.draw(win)
                except:
                    Instruction.update("File not found. Save your file in pics folder in .gif format.")
        elif Prev_data.includes(pt):
            fprev=open("data\\prev.ax","r")
            lines = [line.rstrip('\n') for line in fprev]
            Pic_name.insert(lines[0])
            F_name.insert(lines[8])
            ThisGraph=GraphArea(float(lines[9]),float(lines[10]),float(lines[11]),float(lines[12]),float(lines[13]),float(lines[14]),float(lines[15]),float(lines[16]),float(lines[17]),float(lines[18]),)
            ThisGraph.clearAxes()
            lines.clear()
            fprev.close()
        elif TwoD.includes(pt):
            TwoD.check()
            ThreeD.uncheck()
            I_lin.available()
            I_lan.available()
            I_near.available()
            I_invsq.available()
            I_trend.unavailable()
            Z_cal.unavailable()
        elif ThreeD.includes(pt):
            TwoD.uncheck()
            ThreeD.check()
            I_lin.unavailable()
            I_lan.available()
            I_near.available()
            I_invsq.available()
            I_trend.unavailable()
            Z_cal.available()
        elif I_lin.includes(pt):
            I_lin.check()
            I_lan.uncheck()
            I_near.uncheck()
            I_invsq.uncheck()
            I_trend.uncheck()
        elif I_lan.includes(pt):
            I_lin.uncheck()
            I_lan.check()
            I_near.uncheck()
            I_invsq.uncheck()
            I_trend.uncheck()
        elif I_near.includes(pt):
            I_lin.uncheck()
            I_lan.uncheck()
            I_near.check()
            I_invsq.uncheck()
            I_trend.uncheck()
        elif I_invsq.includes(pt):
            I_lin.uncheck()
            I_lan.uncheck()
            I_near.uncheck()
            I_invsq.check()
            I_trend.uncheck()
        elif I_trend.includes(pt):
            I_lin.uncheck()
            I_lan.uncheck()
            I_near.uncheck()
            I_invsq.uncheck()
            I_trend.check()
        elif Open_file.includes(pt):
            x.clear()
            y.clear()
            z.clear()
            TableLabel=TableRow(10,10,80,"X","Y")
            if ThreeD.IsTrue:
                TableLabel.update("X","Y","Z")
            TableData=[]
            i=0
            try:
                fil=open(processFILE(F_name.read()),"r")
                read=csv.reader(fil,delimiter=",")
                for line in read:
                    x.append(float(line[0]))
                    y.append(float(line[1]))
                    if ThreeD.IsTrue:
                        z.append(float(line[2]))
                        TableData.append(TableRow(10,10+(i+1)*V_SIZE,80,math.floor(float(line[0])*1000)/1000,math.floor(float(line[1])*1000)/1000,math.floor(float(line[2])*1000)/1000))
                    else:
                        TableData.append(TableRow(10,10+(i+1)*V_SIZE,80,math.floor(float(line[0])*1000)/1000,math.floor(float(line[1])*1000)/1000))
                    i=i+1
            except:
                Instruction.update("File not found. Include file extension or path. or toggle 2D/3D.")
            finally:
                n=i
                fil.close()
        elif Open_csv.includes(pt):
            x_c.clear()
            y_c.clear()
            z_c.clear()
            if TwoD.IsTrue:
                Table2Label=TableRow(830,10,80,"X")
            if ThreeD.IsTrue:
                Table2Label=TableRow(750,10,80,"X","Y")
            Table2Data=[]
            i=0
            try:
                fil=open(processFILE(F_csv.read()),"r")
                read=csv.reader(fil,delimiter=",")
                for line in read:
                    x_c.append(float(line[0]))
                    if ThreeD.IsTrue:
                        y_c.append(float(line[1]))
                        Table2Data.append(TableRow(750,10+(i+1)*V_SIZE,80,math.floor(float(line[0])*1000)/1000,math.floor(float(line[1])*1000)/1000))
                    elif TwoD.IsTrue:
                        Table2Data.append(TableRow(830,10+(i+1)*V_SIZE,80,math.floor(float(line[0])*1000)/1000))
                    i=i+1
            except:
                Instruction.update("File not found. Include file extension or path.")
            finally:
                n_c=i
                fil.close()
        elif X_cal.includes(pt):
            if I_lin.IsTrue:
                X_val.insert(str(linear2(float(Y_val.read()),n,y,x)))
            if I_lan.IsTrue:
                if TwoD.IsTrue:
                    X_val.insert(str(lagrange2(float(Y_val.read()),n,y,x)))
                if ThreeD.IsTrue:
                    X_val.insert(str(lagrange2(float(Y_val.read()),float(Z_val.read()),n,y,z,x)))
            if I_near.IsTrue:
                if ThreeD.IsTrue:
                    X_val.insert(str(nearest3(float(Y_val.read()),float(Z_val.read()),n,y,z,x)))
                else:
                    X_val.insert(str(nearest2(float(Y_val.read()),n,y,x)))
            if I_invsq.IsTrue:
                if ThreeD.IsTrue:
                    X_val.insert(str(inversesq3(int(N_invsq.read()),float(Y_val.read()),float(Z_val.read()),n,y,z,x)))
                else:
                    X_val.insert(str(inversesq2(int(N_invsq.read()),float(Y_val.read()),n,y,x)))
        elif Y_cal.includes(pt):
            if I_lin.IsTrue:
                Y_val.insert(str(linear2(float(X_val.read()),n,x,y)))
            if I_lan.IsTrue:
                if TwoD.IsTrue:
                    Y_val.insert(str(lagrange2(float(X_val.read()),n,x,y)))
                if ThreeD.IsTrue:
                    Y_val.insert(str(lagrange2(float(X_val.read()),float(Z_val.read()),n,x,z,y)))
            if I_near.IsTrue:
                if ThreeD.IsTrue:
                    Y_val.insert(str(nearest3(float(X_val.read()),float(Z_val.read()),n,x,z,y)))
                else:
                    Y_val.insert(str(nearest2(float(X_val.read()),n,x,y)))
            if I_invsq.IsTrue:
                if ThreeD.IsTrue:
                    Y_val.insert(str(inversesq3(int(N_invsq.read()),float(X_val.read()),float(Z_val.read()),n,x,z,y)))
                else:
                    Y_val.insert(str(inversesq2(int(N_invsq.read()),float(X_val.read()),n,x,y)))
        elif Z_cal.includes(pt):
            if I_lan.IsTrue:
                Z_val.insert(str(lagrange2(float(X_val.read()),float(y_val.read()),n,x,y,z)))
            if I_near.IsTrue:
                Z_val.insert(str(nearest3(float(X_val.read()),float(Y_val.read()),n,x,y,z)))
            if I_invsq.IsTrue:
                Z_val.insert(str(inversesq3(int(N_invsq.read()),float(X_val.read()),float(Y_val.read()),n,x,y,z)))
        elif InterpolateZ.includes(pt):
            z_c.clear()
            if I_lin.IsTrue:
                for i in range(n_c):
                    y_c.append(linear2(x_c[i],n,x,y))
            if I_lan.IsTrue:
                for i in range(n_c):
                    if ThreeD.IsTrue:
                        z_c.append(lagrange3(x_c[i],y_c[i],n,x,y,z))
                    else:
                        y_c.append(lagrange2(x_c[i],n,x,y))
            if I_near.IsTrue:
                for i in range(n_c):
                    if ThreeD.IsTrue:
                        z_c.append(nearest3(x_c[i],y_c[i],n,x,y,z))
                    else:
                        y_c.append(nearest2(x_c[i],n,x,y))
            if I_invsq.IsTrue:
                for i in range(n_c):
                    if ThreeD.IsTrue:
                        z_c.append(inversesq3(int(N_invsq.read()),x_c[i],y_c[i],n,x,y,z))
                    else:
                        y_c.append(inversesq2(int(N_invsq.read()),x_c[i],n,x,y))
            if ThreeD.IsTrue:
                Table2Label.update("X","Y","Z")
            else:
                Table2Label.update("X","Y")
            for i in range(min(n_c,TABLE_MAX)):
                if ThreeD.IsTrue:
                    Table2Data[i].update(math.floor(1000*x_c[i])/1000,math.floor(1000*y_c[i])/1000,math.floor(1000*z_c[i])/1000)
                else:
                    Table2Data[i].update(math.floor(1000*x_c[i])/1000,math.floor(1000*y_c[i])/1000)
        elif Save_csv.includes(pt):
            fil=open(processFILE(F_csv.read(),"w"),"w",newline='')
            write=csv.writer(fil,delimiter=",")
            for i in range(n_c):
                if TwoD.IsTrue:
                    write.writerow([x_c[i],y_c[i]])
                if ThreeD.IsTrue:
                    write.writerow([x_c[i],y_c[i],z_c[i]])
            fil.close()
            Instruction.update("The interpolated value was saved in to a file in the same directory as the file.")
#InterFromFILE()