import random
import turtle


def coinFlip(n):
    heads = 0
    for i in range(n):
        flip = random.random()
        if flip >= 0.5:
            heads = heads + 1
    float_num = heads/n
    return float_num

def diceGame(n):
    black_dice_higher = 0
    for i in range(n):
        white_dice = random.randint(1,6)
        black_dice = random.randint(1,6)
        if black_dice > white_dice:
            black_dice_higher = black_dice_higher + 1
    test_result = black_dice_higher/n
    return test_result


def highLow(n, min, max):
    higher_result = 0
    high_low = random.randint(min, max)
    print(high_low)
    for i in range(n):
        integer = random.randint(min, max)
        if integer > high_low:
            higher_result = higher_result + 1
    high_low_result = higher_result / n
    return high_low_result

def alwaysOddRoulette(n):
    money = 0
    for i in range(n):
        num = random.randint(0,36)
        even = num % 2
        if even == 0:
            money = money - 1
        else:
            money = money + 1
    return money

def randomBullsEye():
    a = random.randint(50,100)
    b = random.randint(50, 100)
    c = random.randint(50, 100)
    if a > b and a > c:
        max = a
        if b > c:
            med = b
            min = c
        else:
            min = b
            med = c
    if b > a and b > c:
        max = b
        if a > c:
            med = a
            min = c
        else:
            med = c
            min = a
    if c > a and c > b:
        max = c
        if a > b:
            med = a
            min = b
        else:
            med = b
            min = c
        t= turtle.Turtle()
        t.pendown()
        t.circle(max)
        t.fillcolor("red")
        t.circle(med)
        t.fillcolor("white")
        t.circle(min)
        t.fillcolor("red")
















