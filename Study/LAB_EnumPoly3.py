# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-17 07:40:06
# FILE: LAB_EnumPoly3.py
# AUTHOR: Randall Nagy
#
import turtle
from StateSaver.EnumPoly import Enumerator

def draw_circle(zangle, zargs):
    turtle.home()
    turtle.left(zangle)
    turtle.forward(zargs["length"])
    turtle.dot(zargs["size"], zargs["color"])
    if False:
        turtle.left(90)
        turtle.forward(zargs["length"])
        turtle.dot(25, zargs["color"])


if __name__ == "__main__":
    # Note: Statement location & order!
    size = (400, 300)                   # New
    turtle.screensize(size[0],size[1])  # New
    turtle.setup(size[0]/2, size[1]/2)  # New
    
    turtle.ht()
    turtle.speed(0)
    turtle.delay(0)
        
    dots = Enumerator(12)
    values = [
        {"length":50, "color":'red', 'size':10},
        {"length":100, "color":'green', 'size':20},
        {"length":150, "color":'blue', 'size':30},
        {"length":200, "color":'yellow', 'size':40}
        ]
    dots.enum(draw_circle, values[0])
    dots.enum(draw_circle, values[1])
    dots.enum(draw_circle, values[2])
    dots.enum(draw_circle, values[3])
        
    turtle.mainloop()



