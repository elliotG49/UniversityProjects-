def sayhello():
    usr_input = str(input("Please enter your name: "))
    print(usr_input)


def sayhello2():
    print("Hello")
    print("Word")


def euro2pounds():
    usr_input = int(input("PLease enter how many euros you want to convert: "))
    pounds = usr_input * 0.85
    print(usr_input, "converts to", pounds)


def sumdifference():
    x = int(input("Please enter the first number: "))
    y = int(input("Please enter the second number: "))
    diff = x - y
    sumof = x + y
    print("the difference is", diff, "and the sum is", sumof)


def changecounter():
    x = int(input("How many 1ps do you have?: "))
    y = int(input("How many 2ps do you have?: "))
    g = int(input("How many 5ps do you have?: "))
    total = x + (2*y) + (5*g)
    print("You have", total, "amount of money")


def tenhellos():
    for i in range(10):
        print("Hello World")


def countto():
    x = int(input("Please enter a number: "))
    for i in range(0, x):
        print(i)


def zoomzoom():
    x = int(input("Please enter a number: "))
    for i in range(x):
        print("zoom", i,)


def weightstable():
    for i in range(0, 101):
        print('{}{:8} {:.2f}{}'.format(i, "kg",   i*2.2, "Ibs"))


def futurevalue():
    years = int(input("Please enter how many years you wish to invest: "))
    amount = float(input("Please enter how much you wish to invest: "))
    for i in range(years + 1):
        print('{} {} {} {:.2f}{}'.format("in", i, "years you will have", amount * 1.05 ** i, "£"))
        print()


weightstable()