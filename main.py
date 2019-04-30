
from classes import*
from interpolater3D import*
from inter3d import*
from rating import*
def main():
    clearScreen(win)
    Myimg=Image(Point(650,300),"pics\\main_bg.gif")
    Myimg.draw(win)
    InterIMG=Button(" ",250,210,400,50,1)
    InterFILE=Button(" ",750,210,400,50,1)
    Rating=Button(" ",250,360,400,50,1)
    ManageFILE=Button(" ",750,360,400,50,1)
    ManageFILE.unavailable()
    VisitFB=Button("",1150,450,200)
    Exit=Button("",40,520,75)
    info=Writing("ZeroSofts",1200,535)
    info._Text.setSize(20)
    pt=win.getMouse()
    if InterIMG.includes(pt):
        InterFromIMG()
    elif InterFILE.includes(pt):
        InterFromFILE()
    elif Rating.includes(pt):
        RatingFromFILE()
    elif Exit.includes(pt):
        exit(1)
    elif VisitFB.includes(pt):
        system("explorer \"http://www.facebook.com/atreyagaurav54\"")
while True:
    try:
        main()
    except BaseException:
        break
    except:
        break