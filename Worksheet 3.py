# Practical Worksheet P3: Graphical Programming
# Elliot GArdner-Medwin, 2068521

from time import perf_counter
from graphics import *


def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    arms = Line(Point(70, 90), Point(130, 90))
    left_leg = Line(Point(100, 120), Point(70, 150))
    right_leg = Line(Point(100, 120), Point(130, 150))
    left_leg.draw(win)
    arms.draw(win)
    right_leg.draw(win)
    body.draw(win)
    time.sleep(2)


def Draw_circle():
    radius = float(input("Please enter a radius: "))
    win = GraphWin("Circle", 500, 500)
    centre = Point(250, 250)
    cir = Circle(centre, radius)
    cir.draw(win)
    time.sleep(2)


def Draw_Achery_Target():
    win = GraphWin("Window", 500, 500)
    centre = Point(250, 250)
    blue = Circle(centre, 90)
    blue.setFill('blue')
    blue.draw(win)
    red = Circle(centre, 60)
    red.setFill('red')
    red.draw(win)
    yellow = Circle(centre, 30)
    yellow.setFill('yellow')
    yellow.draw(win)
    time.sleep(2)


def draw_rectangle():
    height = int(input("Please enter the height: "))
    width = int(input("Please enter the width: "))
    win = GraphWin("window", 500, 500)
    centre = Point(250, 250)
    rec = Rectangle(Point(250+width, 250+height), Point(250-width, 250-height))
    rec.draw(win)
    win.getMouse()


def blue_circle():
    win = GraphWin("window", 500, 500)
    x = win.getMouse()
    cir = Circle(x, 50)
    cir.setFill('blue')
    cir.draw(win)
    cir.move(10, 50)
    win.getMouse()


def drawLine():
    win = GraphWin("Line drawer", 500, 500)
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText()

def tenstrings():
    win = GraphWin("Greeter", 500, 500)
    for i in range(10):
        inputBox = Entry(Point(200, 200), 10)
        inputBox.draw(win)
        p = win.getMouse()
        t = Text(p, inputBox.getText())
        t.draw(win)
        time.sleep(0.5)
    
def tenrectangles():
    win = GraphWin("rectangle", 500, 500)
    for i in range(10):
        inputBox = Entry(Point(250, 50), 10)
        inputBox.draw(win)
        p1 = win.getMouse()
        p1X = p1.getX()
        p1Y = p1.getY()
        p2 = win.getMouse()
        p2X = p2.getX()
        p2Y = p2.getY()
        rec =  Rectangle(Point(p1X,p1Y), Point(p2X, p2Y))
        rec.setFill(inputBox.getText())
        rec.draw(win)
        time.sleep(1)

def fiveClickStickFigure():
    win = GraphWin("Stick figure", 500, 500)
    centre = win.getMouse() #centre of cirlce
    centreX = centre.getX()
    centreY = centre.getY()
    radius_click = win.getMouse()
    radiusX = radius_click.getX()
    radiusY = radius_click.getY()
    radius = radiusX - centreX
    head = Circle(centre, radius)
    head.draw(win)
    bodyline = win.getMouse()
    bodyX = bodyline.getX()
    bodyY = bodyline.getY()
    body = Line(Point(bodyX, bodyY), Point(centreX, centreY+radius)) 
    body.draw(win)
    armline = win.getMouse()
    armX = armline.getX()
    armY = armline.getY()
    legnth = centreX - armX
    arm1 = Line(Point(armX, armY), Point(centreX, armY))
    arm2 = Line(Point(centreX, armY), Point(centreX+legnth, armY))
    arm1.draw(win)
    arm2.draw(win)
    legline = win.getMouse()
    legX = legline.getX()
    legY = legline.getY()
    length2 = bodyX - legX
    leg1 = Line(Point(legX, legY), Point(bodyX, bodyY))
    leg2 = Line(Point(bodyX, bodyY), Point(bodyX+length2, legY))
    leg1.draw(win)
    leg2.draw(win)
    win.getMouse()

drawLine()
   
