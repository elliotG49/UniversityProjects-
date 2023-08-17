import math
from graphics import *
import string 
import re
import random
import hashlib

# sentence = "I saw a wolf in the forest. A lonely wolf."
# print(sentence)
# word = input("Enter the word to find: ")
# position = sentence.find(word)
# print("The word",word,"is at character",position)

# upper()
# Example code: 	x = y.upper()
# Purpose: To turn a string into uppercase.
# x is the name of the variable to return the result to.  y is the original variable.

# .lower()
# Example code: 	x = y.lower()
# Purpose: To turn a string into lowercase.

# len()
# Example code: 	x = Len(y)
# Purpose: To return the number of characters in a string.
# x becomes the number of characters in y.

# [:?]
# Example code: 	x = y[:z]
# Purpose: To return characters to the left of a string.
# x becomes the characters.  y is the string to extract characters from.  z is the number of characters to extract from the left.

# [-?:]
# Example code: 	x = y[-z:]
# Purpose: To return characters to the right of a string.
# x becomes the characters.  y is the string to extract characters from.  z is the number of characters to extract from the right.

# [?:?]
# Example code: 	x = y[w:z]
# Purpose: To extract characters from the middle of a string.
# x becomes the middle characters of y, starting from position w, up to z number of characters.

# .find()
# Example code: 	x = y.find(z)
# Purpose: To find the position of substring z in y.
# X becomes the position in the string y where z can be found. E.g. x = “Hello World”.find(”World”) returns 6 as the letter W is the sixth character in the string (starting at zero).

# .format
# print('{}{:8} {:.2f}{}'.format(i, "kg",   i*2.2, "Ibs"))

# ==	equals
# <	less than
# and both conditions must be true
# !=	does not equal
# <=	less than or equal to	or	one condition must be true
# >	greater than	not	condition is not true
# >=	greater than or equal to

# binary write mode
# open("filename.txt", "wb")
# file.close()
# print(file.read(4))
# print(file.readlines())

# easy loop to read all lines=
# for line in files:
#    print(line)
#flie.close
# to find out how many lines there are in a file
#len(open("text.txt").readlines())

# IMPORT STRING:
# string.ascii_lowercase
# string.ascii_uppercase
# string.digits
# string.hexdigits
# string.octdigits
# string.punctuation

def circumference(r):
    c = 2 * math.pi * r
    return c 

def AreaOfCircle(r):
    a = math.pi * (r**r)
    return a 

def slope_of_line(y1, y2, x1, x2):
    slope = (y2 - y1) / (x2 - x1)
    print("THe slope of the line between the two points is: ", slope)

def distance_between_two_points(y1, y2, x1, x2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def fibonacci(nterms):
    n1 = 0
    n2 = 1
    count = 2
    print("Fibonacci sequence upto", nterms, ":")
    print(n1, ",", n2, ', ')
    while count < nterms:
        nth = n1 + n2
        print(count, nth, ", ")
        n1 = n2
        n2 = nth
        count += 1

def arc_length(circumference, ark):
    arc_length = (circumference * ark) / 360
    return arc_length

def using_search():
    x = True
    while x:
        email = input("Please enter your email: ")
        print()
        if not re.search("[a-z]", email):
            print("Email not valid, try again")
            print()
        elif not re.search("[@]", email):
            print("Email not valid, try again")
            print()
        elif not re.search("[.com]", email):
            print("Email not valid, try again")
            print()
        else:
            print("Valid Email.")
            print()
            print()
            x = False

def name_seperator(fullname):
    space = fullname.find(' ')
    firstname = fullname[:space]
    surname = fullname[space:]

def hashing(message):
    message_enc  = str.encode(message, "utf-8")
    hash = hashlib.sha256(message_enc.strip()).hexdigest()
    return hash

def conversion():
    usr_input = int(input("PLease enter how many euros you want to convert: "))
    pounds = usr_input * 0.85
    print(usr_input, "converts to", pounds)

def investing():
    years = int(input("Please enter how many years you wish to invest: "))
    amount = float(input("Please enter how much you wish to invest: "))
    for i in range(years + 1):
        print('{} {} {} {:.2f}{}'.format("in", i, "years you will have", amount * 1.05 ** i, "£"))

def random_gen(x, y):
    r1 = random.randint(x, y)

def read_char_from_file():
    file = open("/usercode/files/books.txt", "r")
    contents = file.readlines()
    lg1 = len(contents[0]) -1
    lg2 = len(contents[1]) -1
    lg3 = len(contents[2]) -1
    lg4 = len(contents[3])
    file.close()

    line1 = contents[0]
    first_char1 = line1[0]

    line2 = contents[1]
    first_char2 = line2[0]

    line3 = contents[2]
    first_char3 = line3[0]

    line4 = contents[3]
    first_char4 = line4[0]

def formalname2(forename, surname):
    fInitial = forename[0:1]
    name = f'{fInitial.upper()},{surname.upper()} '

    print(name)

def graphicletters():
    x = str(input("Please enter a word: "))
    win = GraphWin("window", 500, 500)
    
    for i in range(10):
        point = win.getMouse()
        text = Text((point), x)
        text.setSize(20)
        text.setFill('red')
        text.draw(win)

def new_lines():
    x = str(input("Please enter a word: "))
    times = int(input("Please enter how many times the word should be repeated in the song: "))
    lines = int(input("How many lines would you like to be?: "))
    y = (x + ", ")*times
    for i in range(lines):
        print(y, "\n")

def split_words_into_first_letters(txt):
    x = txt.split()
    for word in txt.split(): print(word[0])

def nameToNumber():
    letters = string.ascii_lowercase
    x = list(letters)
    user = str(input("please enter your name: "))
    y = list(user)
    length = len(y)
    pos1 = x.index(y[0]) + 1
    pos2 = x.index(y[1]) + 1
    pos3 = x.index(y[2]) + 1
    total = pos1+pos2+pos3
    print(total)

def file_in_caps():
    filename = str(input("Please enter the file name: "))
    filename = str(filename + '.txt')
    file = open(filename, "w")
    file.write("the name of your file is: " + filename)
    file = open(filename, "r")
    contents = file.read()
    print(str.upper(contents))
    file.close()


#             -----GRAPHICS-----
# 
# 
# shape.setWidth(3)
# shape.setOutline("cyan")
# shape.setFill("green")
# shape.move(10, 20)
# shape.getRadius()
# p.getX()
# p.getY()
# triangle = Polygon(Point(100, 20), Point(120, 80), Point(140, 10))

# 
# 


def Draw_circle(win, centre, radius, colour):
    cir = Circle(centre, radius)
    cir.setFill(colour)
    cir.draw(win)

def draw_tri(p1, p2, p3, colour, outline, win): # basic function to draw a triangle
    tri = Polygon(p1, p2, p3)
    tri.setOutline(outline)
    tri.setFill(colour)
    tri.draw(win)

def draw_rec(p1, p2, colour, outline, win): # basic function to draw a rectangle
    rec = Rectangle(p1, p2)
    rec.setFill(colour)
    rec.setOutline(outline)
    rec.draw(win)

def tenstrings():
    win = GraphWin("Greeter", 500, 500)
    for i in range(10):
        inputBox = Entry(Point(200, 200), 10)
        inputBox.draw(win)
        p = win.getMouse()
        t = Text(p, inputBox.getText())
        t.draw(win)
        time.sleep(0.5)

def draw_line(p1, p2, colour, width, win):
    line1 = Line(p1, p2)
    line1.setFill(colour)
    line1.setWidth(width)
    line1.draw(win)

def move_prac():
    radius = int(input("Please enter a radius: "))
    win = GraphWin("Circle", 500, 500)
    centre = Point(250, 250)
    cir = Circle(centre, radius)
    cir.draw(win)
    time.sleep(1)
    cir.move(100, 100)

    time.sleep(2)

    
move_prac()







