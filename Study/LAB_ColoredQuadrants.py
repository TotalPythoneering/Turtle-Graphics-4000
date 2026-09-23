# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-12 04:34:04
# FILE: LAB_ColoredQuadrants.py
# AUTHOR: Randall Nagy
#
import turtle


def color_circle(xcord, ycord, zwidth, zcolor='black'):
    from StateSaver import Stack
    stack = Stack.Stack()
    stack.push()
    turtle.pensize(10)
    turtle.penup();turtle.goto(xcord, ycord)
    turtle.pendown()
    turtle.dot(zwidth, zcolor)
    stack.pop()

color_circle(100, 100, 200, "green")
color_circle(-100, 100, 150, "blue")
color_circle(100, -100, 100, "aqua")
color_circle(-100, -100, 50, "red")

turtle.mainloop()




