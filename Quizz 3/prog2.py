#Raúl Adolfo Torres Vargas
#A01400187
#Quiz #3 program 2

def fibonaccinumber(num):
    a = int(1)
    c = int(0)
    b = int(0)
    for n in range(num):
        b = a + b
        a = c
        c = b
    return c

num = int(input("Please give me a number to evaluate: "))

print(fibonaccinumber(num))

def fibonacciserie(num):
    a = int(0)
    b = int(1)
    c = int(0)
    for i in range(1,num):
        c = a + b
        a = b
        b = c
        print(c, end=",")
    return c
num = int(input("Please enter the number to start the fibonacci sequence: "))
print(fibonacciserie(num))
