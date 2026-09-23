# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-18 07:08:42
# FILE: LAB_EnumCircle01.py
# AUTHOR: Randall Nagy
# LAB_EnumCircle01.py
# (RESEARCH PHASE)
#

import turtle

def draw_circle(zangle, zargs):
    turtle.up()
    turtle.degrees(zargs["size"])
    turtle.pencolor(zargs["color"])
    turtle.home()
    turtle.left(zangle)
    turtle.forward(100)
    turtle.down()
    turtle.circle(50, zargs["length"], 12)

turtle.ht()
degrees_per = 360
qtr = degrees_per/4
model = {"length":qtr*1, "color":'red', 'size':degrees_per}
draw_circle(90, model)
turtle.mainloop()



