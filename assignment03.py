import math
def multiply(a,b):
    acc = 0
    for i in range(a):
        acc = acc + b
    return acc

def power(a,b):
    acc = 1
    for i in range(b):
        acc = acc * a
    return acc
def factorial(n):
    acc = 1
    for i in range(1,n+1):
        acc = acc * i
    return acc
def triangularSeries(sideLength):
    result = 0
    for col in range(1, sideLength+1):
        result = result + col
    return result

# def triangularSeries(t,sideLength):
#     for col in range(sideLength):
#         for row in range(sideLength):
#             t.dot()
#             t.forward(sideLength)
def fibonacci(n):
    first = 1
    second = 1
    for i in range(2, n):
        sum = first + second
        first = second
        second = sum
    return sum

def Fibonnacci(myTurtle,n):
    for i in range(2, n):
        myTurtle.right(90)
        myTurtle.forward(n)
    return








