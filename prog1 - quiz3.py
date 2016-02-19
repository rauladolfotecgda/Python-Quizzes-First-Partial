#Raúl Adolfo Torres Vargas
#A01400187
#Quiz #3 program 1

import math
def distance2points(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 +(y2-y1)**2)

x1 = float(input("Please give me the value of x1: "))
y1 = float(input("Please give me the value of y1: "))
x2 = float(input("Please give me the value of x2: "))
y2 = float(input("Please give me the value of y2"))

print(round(distance2points(x1,y1,x2,y2)))

def distance(a,b):
    return math.sqrt((a**2) + (b**2))
a = float(input("Please give me the value of a: "))
b = float(input("Please give me the value of b: "))

print(distance(a,b))