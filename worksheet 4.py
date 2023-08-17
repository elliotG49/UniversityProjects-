from graphics import *
import string


def greeting():
    name = str(input("enter ur name "))
    age = float(input("enter ur age "))
    print("Hello {} you are {:.2f} years old".format(name, age))


def formalname2():
    forename = input("Please enter your first name")
    surname = input("Please enter your Last name")

    fInitial = forename[0:1]
    name = f'{fInitial.upper()}.{surname.upper()} '

    print(name)


def kilos2pounds():
    x = float(input("Please enter a value you would like to convert in kg: "))
    y = x * 2.2
    print("{:.2f} kg's is equal to {:.2f} Ibs".format(x, y))


def email():
    fname = str(input("Please enter your forename: "))
    sname = str(input("Please enter your second name: "))
    date = str(input("Pleade enter the year you enter university: "))
    fname2 = fname[0:1]
    sname2 = sname[0:4]
    date2 = date[:-2]
    print("your email is, {}.{}.{}@myport.ac.uk".format(sname2, fname2, date2))


def gradetest():
    mark = int(input("Please enter a value between 0 and 10: "))
    if mark > 10:
        print("value is not correct, try again: ")
    elif mark >= 8:
        print("well done you received an A")
    elif mark >= 6:
        print("well doine you received a B")
    elif mark >= 4:
        print("well doine you received a C")
    elif mark >= 0:
        print("well doine you received a D")
    else:
        print("ok")
    

def graphicletters():
    x = str(input("Please enter a word: "))
    win = GraphWin("window", 500, 500)
    
    for i in range(10):
        point = win.getMouse()
        text = Text((point), x)
        text.setSize(20)
        text.setFill('red')
        text.draw(win)


def singasong():
    x = str(input("Please enter a word: "))
    times = int(input("Please enter how many times the word should be repeated in the song: "))
    lines = int(input("How many lines would you like to be?: "))
    y = (x + ", ")*times
    for i in range(lines):
        print(y, "\n")


def exhangetable():
    for i in range(0, 21):
        print('{}{:<5.2f}|{:.2f}{}'.format( i,   i*1.17, "€"))


def makeInitialsm():
    txt = str(input("Please enter a phrase: "))
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


        


formalname2()
