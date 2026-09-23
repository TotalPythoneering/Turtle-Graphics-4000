# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-18 06:55:02
# FILE: LAB_EnumCircle02_360.py
# AUTHOR: Randall Nagy
# LAB_EnumCircle02_360.py
#

import turtle
from StateSaver.EnumPoly import Enumerator as E1

def draw_circle(zangle, zargs):
    turtle.up()
    turtle.degrees(zargs["size"])
    turtle.pencolor(zargs['color'])
    turtle.home()
    turtle.left(zangle)
    turtle.forward(100)
    turtle.down()
    turtle.circle(50, zargs["length"], 12)


if __name__ == "__main__":
    turtle.screensize(400, 300)
    
    turtle.ht()
    turtle.speed(0)
    turtle.delay(0)

    degrees_per = 100
    turtle.degrees(degrees_per)
    qtr = degrees_per/4      
    values = [
        {"length":qtr, "color":'red', 'size':degrees_per},
        {"length":qtr*2, "color":'green', 'size':degrees_per},
        {"length":qtr*3, "color":'blue', 'size':degrees_per},
        {"length":degrees_per, "color":'yellow', 'size':degrees_per}
        ]

    turtle.pensize(4)
    dots = E1(len(values))
    ss = 0
    for angle in dots.next():
        draw_circle(angle, values[ss])
        ss += 1
        print(turtle.degrees())
        
    turtle.mainloop()



