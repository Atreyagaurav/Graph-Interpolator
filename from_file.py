from classes import*
global win
clearScreen(win)
Myimg=Image(Point(650,300),"pics\\inter_bg1.gif")
Myimg.draw(win)
Instruction=Writing("Welcome to Graph-Interpolator")
Pic_name=EntryBox("Name",1180,V_SPACING*1,20)
Open_curve=Button("Open Curve",1090,V_SPACING*2,130)
Prev_data=Button("Previous Data",1230,V_SPACING*2,130)
X0=EntryBox("X0",1180,V_SPACING*3,20)
Y0=EntryBox("Y0",1180,V_SPACING*4,20)
Xn=EntryBox("Xn",1180,V_SPACING*5,20)
Yn=EntryBox("Yn",1180,V_SPACING*6,20)
Input_curve=Button("Input Curve",1150,V_SPACING*11,250)
while True:
    pt=win.getMouse()
    if Open_curve.includes(pt):
        if Pic_name.read()=="":
            Instruction.update("Type a file name before opening")
        else:
            try:
                Curve=Image(Point(500,250),processIMG(Pic_name.read()))
                Curve.draw(win)
            except:
                Curve.draw(win)
                Instruction.update("File not found. Save your file in pics folder in .gif format.")
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
    elif Input_curve.includes(pt):
        Instruction.update("Origin.")
        pt_o=win.getMouse()
        ox=pt_o.x
        oy=pt_o.y
        Instruction.update("X-axis.")
        pt_x=win.getMouse()
        xx=pt_x.x-ox
        xy=oy-pt_x.y
        Instruction.update("Y-axix.")
        pt_y=win.getMouse()
        yx=pt_y.x=ox
        yy=oy-pt_y.y
        pt=[]
        rpt=[]
        mp=[]
        rpt_o=pt_o
        rpt_x=pt_x
        rpt_y=pt_y
        pox=float(X0.read())
        poy=float(Y0.read())
        pxx=float(Xn.read())
        pyy=float(Yn.read())
        pxy=rpt_o.y
        pyx=rpt_o.x
        Graph=GraphArea(0,0,xx,xy,yx,yy,pox,poy,pxx,pxy,pyx,pyy)
        i=0
        while True:
            Instruction.update("Other points."+str(i)+"points clicked")
            pt.append(win.getMouse())
            pt[i].x=pt[i].x-ox
            pt[i].y=oy-pt[i].y
            mp.append(MarkPoint(pt[i]))
            rpt.append(Graph.realPoint(pt[i]))
            print("Point #"+str(i+1)+": \tX:"+str(rpt[i].x)+"\tY:"+str(rpt[i].y)+"\n")
            i=i+1





