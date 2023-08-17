from tkinter.constants import BOTTOM
from graphics import *
import math

def areaOfCircle(radius):
    a =  math.pi * radius ** 2
    return a 
        
def circumference_of_cirlce(r):
    c = 2 * math.pi * r
    return c 

def circle_info():
    c = circumference_of_cirlce(5)
    a = areaOfCircle(5)
    print('{}{:.3f}{}{:.3f}'.format("the circumference of the circle is ", c, "and the area is ", a))


def drawBrownEyeInCentre():
    win1 = GraphWin("eye", 500, 500)
    p1 = Point(250, 250)
    drawCircle(win1, p1, 60, 'white')
    drawCircle(win1, p1, 30, 'brown')
    drawCircle(win1, p1, 15, 'black')
    win1.getMouse()
    
    
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def draw_block_of_stars(width, height):
    y = ("*")*width
    for i in range(height):
        print(y, "\n")
    

def drawletterE():
    draw_block_of_stars(12, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(5, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(12, 2)




def drawBrownEye(win, centre, radius):
    # win1 = GraphWin("", 500, 500)
    drawCircle(win, centre, radius, 'white')
    drawCircle(win, centre, radius/2, 'brown')
    drawCircle(win, centre, radius/4, 'black')


def draw_pair_of_eyes():
    win = GraphWin("", 500, 500)
    drawBrownEye(win, Point(300, 250), 50)
    drawBrownEye(win, Point(200, 250), 50)
    time.sleep(5)


draw_pair_of_eyes()