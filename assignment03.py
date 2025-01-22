import math

# Function to multiply two numbers using repeated addition
def multiply(a, b):
    acc = 0
    for i in range(a):
        acc = acc + b
    return acc

# Function to calculate the power of a number using repeated multiplication
def power(a, b):
    acc = 1
    for i in range(b):
        acc = acc * a
    return acc

# Function to calculate the factorial of a number
def factorial(n):
    acc = 1
    for i in range(1, n+1):
        acc = acc * i
    return acc

# Function to calculate the sum of the first 'sideLength' natural numbers (triangular series)
def triangularSeries(sideLength):
    result = 0
    for col in range(1, sideLength+1):
        result = result + col
    return result

# Function to calculate the nth Fibonacci number
def fibonacci(n):
    first = 1
    second = 1
    for i in range(2, n):
        sum = first + second
        first = second
        second = sum
    return sum

# Function to draw the Fibonacci sequence using a turtle
def Fibonnacci(myTurtle, n):
    for i in range(2, n):
        myTurtle.right(90)
        myTurtle.forward(n)
    return
