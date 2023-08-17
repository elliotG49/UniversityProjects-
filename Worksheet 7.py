from graphics import *


def calculate_grade(mark):
    if mark > 20 or mark < 0:
        return ("X")
    elif mark >= 12 and mark <= 20:
        return ("A")
    elif mark >= 8 and mark < 12:
        return ("B")
    else:
        return ("F")


def get_name():

    name = True

    while (name):
        name = input("name: ")
        if name.isalpha():
            name = False
            return name


def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        red.setFill('red')
        time.sleep(3)
        amber.setFill('yellow')
        time.sleep(2)
        amber.setFill('black')
        red.setFill('black')
        green.setFill('green')
        time.sleep(3)
        green.setFill('black')


def grade_coursework():
    






trafficLights()
