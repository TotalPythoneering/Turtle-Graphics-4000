# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-06 07:45:06
# FILE: LAB_SpotOn.py
# AUTHOR: Randall Nagy
# Lab: SpotOn
#

import turtle

# Core:
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.home()
turtle.pensize(3)
turtle.penup()
turtle.goto(-50, -50)
turtle.color('black')
turtle.pendown()
for line in range(4):
    turtle.forward(100)
    turtle.left(90)

# Bonus
turtle.penup()
turtle.home()
turtle.dot(50, 'aqua')
turtle.done()
