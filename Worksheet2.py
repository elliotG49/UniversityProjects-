import math


def circumference_of_circle():
    r = int(input("Please enter the radius of the circle: "))
    c = 2 * math.pi * r
    print("the circumference is", c)


def AreaOfCircle():
    r = int(input("Please enter the radius of the circle: "))
    a = math.pi * (r**r)
    print("The area of the circle is:", a)


def cost_of_pizza():
    d = int(input("Please enter the diameter of the circle: "))
    r = d/2
    a = math.pi * (r**r)
    cost = a/1.5
    print("The ingredients will cost: ", cost, "p")


def slope_of_line():
    y1 = int(input("Please enter four values y1: "))
    y2 = int(input("Please enter four values y2 "))
    x1 = int(input("Please enter four values x1: "))
    x2 = int(input("Please enter four values x2: "))
    print()
    slope = (y2 - y1) / (x2 - x1)
    print("THe slope of the line between the two points is: ", slope)


def distance_between_two_points():
    y1 = int(input("Please enter four values y1: "))
    y2 = int(input("Please enter four values y2 "))
    x1 = int(input("Please enter four values x1: "))
    x2 = int(input("Please enter four values x2: "))
    print()
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("the distance between the 2 points are: ", distance)


def travel_stats():
    speed = int(input("Please enter the average speed in km/h: "))
    time = int(input("Please enter the amount of hours the car journey was in km: "))
    print()
    distance = speed * time
    print("the overall distance was: ", distance)
    fuel = distance/5
    print("you used", fuel, "litres of fuel")
    print()


def sum_of_squares():
    x = int(input("Please enter a value: "))
    total = 0
    for i in range(1, x+1):
        total = total + i**2
        print(i, total)


def average_of_numbers():
    x = int(input("Please enter how many values you want to be averaged: "))
    numbers = []
    for i in range(1, x+1):
        y = int(input("Please enter a number" + " " + str(i) + ": "))
        numbers.append(y)
    total = sum(numbers)
    average = total/i
    print("the average of your list is", average)


def fibonacci():
    nterms = int(input("Please enter a value: "))
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


def select_coins():
    value = float(input("Please enter a value in Pence: "))
    coins = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]
    x200 = value // 200
    coins[0] = x200, "2 Pound coins "
    value = value - x200 * 200
    print(coins[0])

    x100 = value // 100
    coins[1] = x100, "1 Pound coins "
    value = value - x100 * 100
    print(coins[1])

    x50 = value // 50
    coins[2] = x50, "50p coins "
    value = value - x50 * 50
    print(coins[2])
    print()

    x20 = value // 20
    coins[3] = x20, "20p coin "
    value = value - x20 * 20
    print(coins[3])

    x10 = value // 10
    coins[4] = x10, "10p coins "
    value = value - x10 * 10
    print(coins[4])

    x5 = value // 5
    coins[5] = x5, "5 pence coins "
    value = value - x5 * 5
    print(coins[5])

    x2 = value // 2
    coins[6] = x2, "2 Pence coins "
    value = value - x2 * 2
    print(coins[6])

    x1 = value // 1
    coins[7] = x1, "1 pence coins "
    value = value - x1 * 1
    print(coins[7])


average_of_numbers()
