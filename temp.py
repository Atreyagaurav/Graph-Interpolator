
from classes import*
MyImg=Image(Point(500,250),"pics\\fy_pers.gif")
MyImg.draw(win)
while True:
	pt=win.getMouse()
	print(str(pt.x)+"\t"+str(pt.y))