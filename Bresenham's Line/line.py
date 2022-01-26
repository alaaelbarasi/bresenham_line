from graphics import *
import time

def bresenhamLine (x1, y1, x2, y2):
    winX = 1500
    winY = 800
    win = GraphWin('Bresenham\'s Line', winX, winY)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x=x1
    y=y1
    p=2*dy-dx
    while(x<x2):
        if(p>=0):
            y+=1
            p+=2*dy-2*dx
        else:
            p+=2*dy
        putPixel(win,x,y)
        x+=1
        time.sleep(0.01)  
    win.getMouse() 
    win.close()    

def putPixel(win,x,y):
         pt= Point(x,y)
         pt.draw(win)

def main():
   x1,y1 = [int(x) for x in input("Enter the value of x1 and y1 : ").split()]
   x2,y2=[int(x) for x in input("Enter the value of x2 and y2 : ").split()]
   bresenhamLine (x1, y1, x2, y2)

if __name__ == "__main__":
   main()