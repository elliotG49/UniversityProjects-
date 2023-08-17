hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter rate")
r = float(rate)
if h < 40:
    pay = r*h
    else h > 40:
    pay = 1.5*r*h
print ("Pay", pay)