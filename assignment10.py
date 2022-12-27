def printStarTriangleDecreasingLeft(n):
    if n > 0:
        print(n * "*")
        printStarTriangleDecreasingLeft(n-1)
    else:
        return

def printStarTriangleDecreasingRight(n):
    printStarDecreasingRightHelper(n, 0)

def printStarDecreasingRightHelper(n,h):
    if n > 0:
        # print("*", end="")
        print(h * " " + n * "*")
        printStarDecreasingRightHelper(n - 1, h + 1)

    else:
        return

def printStarTriangleIncreasingLeft(n):
    if n > 0:
        printStarTriangleIncreasingLeft(n-1)
        print(n * "*")
    else:
        return
def printStarTriangleIncreasingRight(n):
    printStarTriangleIncreasingRightHelper(n, 0)

def printStarTriangleIncreasingRightHelper(n,h):
    if n > 0:
        # print("*", end="")
        printStarTriangleIncreasingRightHelper(n - 1, h + 1)
        print(h * " " + n * "*")

    else:
        return
def printHourGlassTopHelper(n,h):
    if n > 0:
        print(h * " " + n * "*")
        printHourGlassTopHelper(n-2, h + 1)
    else:
        return
def printHourGlassTop(n):
    printHourGlassTopHelper(n,0)

def printHourGlassBottomHelper(n,h):
    if n > 0:
        printHourGlassBottomHelper(n-2, h + 1)
        print(h * " " + n * "*")
    else:
        return
def printHourGlassBottom(n):
    printHourGlassBottomHelper(n, 0)#

def binaryToDecimal(s):
    if len(s) == 0:
        return 0
    return binaryToDecimalHelper(s,0)

def binaryToDecimalHelper(s,n):
    if len(s) > 0:
        acc = int(s[-1]) * (2**n)
        # if int(s[-1]) == 1:
        #     chr = 2**n
        return acc + binaryToDecimalHelper(s[:-1], n+1)
    else:
        return 0

def decimalToBinary(n):
    if n == 0:
        return str(0)
    s = ""
    return decimalToBinaryHelper(n,s)

def decimalToBinaryHelper(n,s):
    if n >= 1:
        return (decimalToBinaryHelper(n//2,s)) + str(n % 2)
    return ""
