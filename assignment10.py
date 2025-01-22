# Function to print a left-aligned decreasing triangle of stars
def printStarTriangleDecreasingLeft(n):
    if n > 0:
        print(n * "*")
        printStarTriangleDecreasingLeft(n-1)
    else:
        return

# Function to print a right-aligned decreasing triangle of stars
def printStarTriangleDecreasingRight(n):
    printStarDecreasingRightHelper(n, 0)

# Helper function for right-aligned decreasing triangle of stars
def printStarDecreasingRightHelper(n, h):
    if n > 0:
        print(h * " " + n * "*")
        printStarDecreasingRightHelper(n - 1, h + 1)
    else:
        return

# Function to print a left-aligned increasing triangle of stars
def printStarTriangleIncreasingLeft(n):
    if n > 0:
        printStarTriangleIncreasingLeft(n-1)
        print(n * "*")
    else:
        return

# Function to print a right-aligned increasing triangle of stars
def printStarTriangleIncreasingRight(n):
    printStarTriangleIncreasingRightHelper(n, 0)

# Helper function for right-aligned increasing triangle of stars
def printStarTriangleIncreasingRightHelper(n, h):
    if n > 0:
        printStarTriangleIncreasingRightHelper(n - 1, h + 1)
        print(h * " " + n * "*")
    else:
        return

# Helper function to print the top part of an hourglass shape
def printHourGlassTopHelper(n, h):
    if n > 0:
        print(h * " " + n * "*")
        printHourGlassTopHelper(n-2, h + 1)
    else:
        return

# Function to print the top part of an hourglass shape
def printHourGlassTop(n):
    printHourGlassTopHelper(n, 0)

# Helper function to print the bottom part of an hourglass shape
def printHourGlassBottomHelper(n, h):
    if n > 0:
        printHourGlassBottomHelper(n-2, h + 1)
        print(h * " " + n * "*")
    else:
        return

# Function to print the bottom part of an hourglass shape
def printHourGlassBottom(n):
    printHourGlassBottomHelper(n, 0)

# Function to convert a binary string to a decimal number
def binaryToDecimal(s):
    if len(s) == 0:
        return 0
    return binaryToDecimalHelper(s, 0)

# Helper function for binary to decimal conversion
def binaryToDecimalHelper(s, n):
    if len(s) > 0:
        acc = int(s[-1]) * (2**n)
        return acc + binaryToDecimalHelper(s[:-1], n+1)
    else:
        return 0

# Function to convert a decimal number to a binary string
def decimalToBinary(n):
    if n == 0:
        return str(0)
    s = ""
    return decimalToBinaryHelper(n, s)

# Helper function for decimal to binary conversion
def decimalToBinaryHelper(n, s):
    if n >= 1:
        return (decimalToBinaryHelper(n//2, s)) + str(n % 2)
    return ""
These comments should help explain the purpose and functionality of each part of your code. If you have any other questions or nee
