import turtle
from drawShapes import *

# Create a turtle object
t = turtle.Turtle()
squareLength = 36

# Draw a square
drawPolygon(t, squareLength, 4)
t.forward(squareLength)

# Draw a filled square
drawFilledPolygon(t, squareLength, 4)
t.right(90)
t.forward(squareLength)

# Draw another filled square
drawFilledPolygon(t, squareLength, 4)
t.left(90)

# Draw another square
drawPolygon(t, squareLength, 4)
t.forward(squareLength)
t.left(90)
t.forward(squareLength)
t.right(90)

# Move the turtle to a new position without drawing
t.penup()
t.forward(squareLength)
t.forward(squareLength)
t.pendown()

# Draw a filled triangle
drawFilledPolygon(t, squareLength, 3)
t.right(60)

# Draw a triangle
drawPolygon(t, squareLength, 3)
t.right(60)

# Draw another filled triangle
drawFilledPolygon(t, squareLength, 3)
t.forward(squareLength)
t.left(60)
t.left(60)

# Draw another filled triangle
drawFilledPolygon(t, squareLength, 3)
t.forward(squareLength)
t.left(60)

# Move the turtle to a new position without drawing
t.penup()
t.forward(squareLength)
t.right(60)
t.forward(squareLength)
t.pendown()

# Draw a pentagon
drawPolygon(t, squareLength, 5)
t.forward(squareLength * 0.52)
t.right(30)

# Draw a filled pentagon
drawFilledPolygon(t, squareLength * 0.77, 5)

# Wait for a click to exit
turtle.exitonclick()
