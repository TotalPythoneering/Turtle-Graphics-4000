# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-18 04:30:18
# FILE: LAB_PolygonCircles.py
# AUTHOR: Randall Nagy
# LAB_PolygonCircles
#

import turtle

turtle.screensize(400, 400)
turtle.ht()
turtle.pensize(6)
turtle.right(90)
turtle.up(); turtle.goto(-200, 250); turtle.down()
radius = 50
for sides in range(3,9):
    turtle.dot(12, 'red')
    color = 'gray'
    if sides % 2:
        color = 'green'
    turtle.pencolor(color)
    turtle.circle(radius, 360, sides)
    turtle.up();
    turtle.forward(radius * 2);
    # turtle.left(45)
    turtle.down()

