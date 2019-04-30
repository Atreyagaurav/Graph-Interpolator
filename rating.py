

from classes import*
def RatingFromFILE():
    global win
    clearScreen(win)
    Myimg=Image(Point(650,300),"pics\\rating.gif")
    Myimg.draw(win)
    pt=win.getMouse()
    Myimg.undraw()
    Myimg=Image(Point(650,300),"pics\\inter_bg.gif")
    Myimg.draw(win)
    x=[]
    y=[]
    z=[]
    ratingH=[]
    ratingA=[]
    ratingP=[]
    ratingQ=[]
    ratingT=[]
    n_r=0
    Instruction=Writing("Open the file with data; previous data will also import the graph.")
    Back=Button("Back",40,520,75)
    Pic_name=EntryBox("Pic Name",1200,V_SPACING*1,15)
    Open_curve=Button("Open Pic",1090,V_SPACING*2,130)
    Prev_data=Button("Previous Data",1230,V_SPACING*2,130)
    F_name=EntryBox("File Name",1200,V_SPACING*3,15)
    Open_file=Button("Load Data from File",1150,V_SPACING*4,200)
    Axis=CheckBox("Input Plot Area",1080,V_SPACING*5)
    HiPrecision=CheckBox("High Precision ",1080,V_SPACING*6)
    Plot=Button("Plot Curves from File",1150,V_SPACING*7,200)
    delH=EntryBox("del H",1200,V_SPACING*8,15)
    delP=EntryBox("Precision",1200,V_SPACING*9,15)
    n_val=EntryBox("Manning's n",1200,V_SPACING*10,15)
    s_val=EntryBox("Slope",1200,V_SPACING*11,15)
    Analyse=Button("Analyse Section",1100,V_SPACING*12,150)
    ratingPlot=Button("Plot",1240,V_SPACING*12,90)
    H_val=EntryBox("H",1100,V_SPACING*13,15)
    Q_val=EntryBox("Q",1100,V_SPACING*14,15)
    P_val=Writing("P:wet perimeter",1080,V_SPACING*15)
    A_val=Writing("A:area",1230,V_SPACING*15)
    H_cal=Button("Calculate",1240,V_SPACING*13,90)
    Q_cal=Button("Calculate",1240,V_SPACING*14,90)
    csv_File=EntryBox("File Name",1160,V_SPACING*16,15)
    Save_csv=Button("Save",1270,V_SPACING*16,50)
    Left=EntryBox("Left",500,550,80)
    Right=EntryBox("Right",500,580,80)
    LeftCopy=Button("Copy",950,550,70)
    RightCopy=Button("Copy",950,580,70)
    Axis.unavailable()
    HiPrecision.unavailable()
    while True:
        pt=win.getMouse()
        if Back.includes(pt):
            return
        elif ratingPlot.includes(pt):
            plt.plot(ratingQ,ratingH)
            plt.show(block=False)
            #ratingGraph=GraphArea(min(ratingQ),min(ratingH),max(ratingQ),max(ratingH),200,450,800,450,200,50)
            #bg=Rectangle(Point(200,50),Point(800,450))
            #bg.setFill('Lime')
            #bg.draw(win)
            #plotPoints(ratingGraph,ratingQ,ratingH)
        elif Plot.includes(pt):
            if Axis.IsTrue:
                pass
            else:
                try:
                    ThisGraph.drawAxes()
                    Instruction.update("Graph Drawn as per previous data")
                except:
                    ThisGraph=GraphArea(min(x),min(y),max(x),max(y),200,450,800,450,200,50)
                    Instruction.update("suitably calculated Graph is drawn")
                finally:
                    plotPoints(ThisGraph,x,y)
        elif Analyse.includes(pt):
            Instruction.update("Analysing the Section")
            global ANALYSIS_PRECISION
            ANALYSIS_PRECISION=float(delP.read())
            ht=min(y[0],y[n-1])-min(y)
            table=[]
            table.append(TableRow(670,25,80,"H","P","A","Q"))
            n_r=floor(ht/float(delH.read()))
            increment=float(delH.read())
            i=increment
            j=0
            ratingH.clear()
            ratingP.clear()
            ratingT.clear()
            ratingA.clear()
            ratingQ.clear()
            while(i<ht):
                try:
                    lev.deleteLevel()
                except:
                    pass
                lev=WaterLevel(ThisGraph,float(delP.read()),i,n,x,y)
                lev.drawLevel()
                ratingH.append(i)
                ratingP.append(lev.Perimeter)
                ratingA.append(lev.Area)
                ratingT.append(lev.TopWidth)
                ratingQ.append(1/float(n_val.read())*pow(lev.Area,5/3)/pow(lev.Perimeter,2/3)*pow(float(s_val.read()),.5))
                table.append(TableRow(670,25+(j+1)*V_SIZE,80,str(floor(i*1000)/1000),str(floor(1000*lev.Perimeter)/1000),str(floor(1000*lev.Area)/1000),str(floor(ratingQ[j]*1000)/1000)))
                i=i+increment
                j=j+1
                #hi
            n_r=len(ratingH)
            Instruction.update("Analysing is Completed.")
        elif H_cal.includes(pt):
            try:
                lev.deleteLevel()
            except:
                pass
            H_val.insert(linear2(float(Q_val.read()),n_r,ratingQ,ratingH))
            lev=WaterLevel(ThisGraph,float(delP.read()),float(H_val.read()),n,x,y)
            lev.drawLevel()
            Instruction.update("Value of Height for given Discharge is calculated.")
            P_val.update("P:"+str(floor(lev.Perimeter*1000)/1000))
            A_val.update("A:"+str(floor(lev.Area*1000)/1000))
        elif Q_cal.includes(pt):
            try:
                lev.deleteLevel()
            except:
                pass
            Q_val.insert(linear2(float(H_val.read()),n_r,ratingH,ratingQ))
            Instruction.update("Value of Discharge for given Height is calculated.")
            lev=WaterLevel(ThisGraph,float(delP.read()),float(H_val.read()),n,x,y)
            lev.drawLevel()
            P_val.update("P:"+str(floor(lev.Perimeter*1000)/1000))
            A_val.update("A:"+str(floor(lev.Area*1000)/1000))
        elif Open_curve.includes(pt):
            Pic_name.insert(processIMG(Pic_name.read()))
            if Pic_name.read()=="":
                Instruction.update("Type a file name before opening")
            else:
                try:
                    Curve=Image(Point(500,250),processIMG(Pic_name.read()))
                    Curve.draw(win)
                except:
                    Instruction.update("File not found. Give correct name and path.")
        elif Prev_data.includes(pt):
            fprev=open("data\\prev.ax","r")
            lines = [line.rstrip('\n') for line in fprev]
            Pic_name.insert(lines[0])
            F_name.insert(lines[8])
            ThisGraph=GraphArea(float(lines[9]),float(lines[10]),float(lines[11]),float(lines[12]),float(lines[13]),float(lines[14]),float(lines[15]),float(lines[16]),float(lines[17]),float(lines[18]))
            ThisGraph.clearAxes()
            lines.clear()
            fprev.close()
        elif Axis.includes(pt):
            Axis.toggle()
            if Axis.IsTrue:
                HiPrecision.available()
            else:
                HiPrecision.unavailable()
        elif HiPrecision.includes(pt):
            HiPrecision.toggle()
        elif Open_file.includes(pt):
            x.clear()
            y.clear()
            z.clear()
            TableLabel=TableRow(10,10,80,"X","Y")
            TableData=[]
            i=0
            try:
                fil=open(processFILE(F_name.read()),"r")
                read=csv.reader(fil,delimiter=",")
                for line in read:
                    x.append(float(line[0]))
                    y.append(float(line[1]))
                    TableData.append(TableRow(10,10+(i+1)*V_SIZE,80,math.floor(float(line[0])*1000)/1000,math.floor(float(line[1])*1000)/1000))
                    i=i+1
            except:
                Instruction.update("File not found. Include file extension or path.")
            finally:
                n=i
                fil.close()
                ht=min(y[0],y[n-1])-min(y)
                delH.insert(str(0.25))
                delP.insert(str(.01))
                n_val.insert(str(.025))
                s_val.insert(str(.005))
        elif Save_csv.includes(pt):
            try:
                csv_File.insert(processFILE(csv_File.read(),"c"))
                fil=open(csv_File.read(),"w",newline='')
                write=csv.writer(fil,delimiter=",")
                write.writerow(["H","P","T","A","Q"])
                for i in range(n_r):
                        write.writerow([ratingH[i],ratingP[i],ratingT[i],ratingA[i],ratingQ[i]])
                Instruction.update("The rating curve data was saved to the file in the location provided.")
            except:
                Instruction.update("Type a file name with path.")
            finally:
                fil.close()
#RatingFromFILE()