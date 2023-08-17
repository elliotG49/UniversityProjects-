# Practical Worksheet 6: if statements and for loops
# your name, your number

import math
import random
from graphics import *

def fast_food_order_price():
    user_price = float(input("Please enter the price of your order: "))
    if user_price > 10:
        print("no delivery fee, your price is", user_price)
    else:
        print("with delivery your price is: ", user_price+1.5, "£")


def whatToDoToday():
    user_input = int(input("please enter the temperature today: "))
    if user_input > 25:
        print("You should swim in the sea!")
    elif user_input >= 15 and user_input < 25:
        print("Shop at gunwarf")
    else:
        print("watch a film at home")


def displaySquareRoots(start, end):
    for i in range(start, end + 1):
        print(i, math.sqrt(i))


def calculate_grade(mark):
    if mark > 20 or mark < 0:
        return ("X")
    elif mark >= 12 and mark <= 20:
        return ("A")
    elif mark >= 8 and mark < 12:
        return ("B")
    else:
        return ("F")


def peasInAPod():
    user_input = int(input("Please enter the number of cirlces: "))
    win = GraphWin("", 100*user_input, 100)
    centre = Point(50, 50)
    cir = Circle(centre, 50)
    cir.draw(win)
    cir.setFill('green')
    centreX = 50
    for i in range(user_input):
        cir = Circle(Point(centreX + 100, 50), 50)
        centreX = centreX + 100
        cir.setFill('green')
        cir.draw(win)
    win.getMouse()


def ticketPrice(age, dist):
    ticket_price = 3 + (0.15*dist)
    if age >= 60 or age <= 15:
        return float(ticket_price * 0.6)
    else:
        return ticket_price


def numberedSquare(n):
    pass


# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawColouredEye(win, centre, radius, colour):
    drawCircle(win, centre, radius, 'white')
    drawCircle(win, centre, radius/2, colour)
    drawCircle(win, centre, radius/4, 'black')
    win.getMouse()


def eyePicker():
    centreX = int(input("enter the centre X cord: "))
    centreY = int(input("enter the centre Y cord: "))
    centre = Point(centreX, centreY)
    radius = int(input("Please enter a radius: "))
    colour = input("Please enter a valid colour: ")
    colList = ["red","green"
    ]
    if colour in colList:
        win = GraphWin("", 500, 500)
        drawCircle(win, centre, radius, 'white')
        drawCircle(win, centre, radius/2, colour)
        drawCircle(win, centre, radius/4, 'black')
        win.getMouse()
    else:
        print("not a valid colour")
            
def drawPatchWindow():
    win = GraphWin("", 200, 200)
    p1 = Point(0, 180)
    p2 = Point(20, 200)
    for i in range(10):
        rec = Rectangle(p1, p2)
        rec.setFill('red')
        rec.draw(win)
        p1 = Point(p1.getX() + 20, p1.getY() - 20)
        p2 = Point(p2.getX() + 20, p2.getY() - 20)
    win.getMouse()


def drawPatch(win, x, y, colour):
    tl = Point(x, y)
    br = Point(x + 20, y + 20)
    rec = Rectangle(tl, br)
    rec.setFill(colour)
    rec.draw(win)
    p1 = Point(tl.getX() + 20, tl.getY() - 20)
    p2 = Point(br.getX() + 20, br.getY() - 20)
    for i in range(9):
        rec = Rectangle(p1, p2)
        rec.setFill(colour)
        rec.draw(win)
        p1 = Point(p1.getX() + 20, p1.getY() - 20)
        p2 = Point(p2.getX() + 20, p2.getY() - 20)

    win.getMouse()


def drawPatchwork():
    pass

def all_eyes_around():
    win = GraphWin("", 500, 500)
    colours = ["blue", "green", "brown", "grey"]
    count = 0

    for i in range(30):
        click = win.getMouse()
        if count > 3:
            count = 0
            drawColouredEye(win, click, 30, colours[count])
        else:
            drawColouredEye(win, click, 30, colours[count])
            count = count + 1
        

def archerygame():
    win = GraphWin("", 500, 500)
    centre = Point(250, 250)
    drawCircle(win, centre, 100, 'blue')
    drawCircle(win, centre, 66, 'red')
    drawCircle(win, centre, 33, 'yellow')
    for i in range(5):
        x = random.randint(1 ,5)
        y = random.randint(1, 5)
        p1 = Point(x, y)
        click = win.getMouse()
        clickmove = Point(click.getX() + x, click.getY() - y)
        drawCircle(win, clickmove, 10, 'black')
        p1 = Point(250, 50)
    score = Text(p1, "SCORE HERE")
    score.draw(win)
    win.getMouse()

    # COULDNT WORK OUT HOW TO DO THE SCORE

drawPatchWindow()





