# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-17 08:38:44
# FILE: LAB_EnumPoly4.py
# AUTHOR: Randall Nagy
#
import turtle
from StateSaver.EnumPoly import Enumerator

def draw_circle(zangle, zargs):
    turtle.up()
    turtle.pencolor(zargs['color'])
    turtle.home()
    turtle.left(zangle)
    turtle.forward(zargs["length"]/2)
    turtle.down()
    size = zargs["size"]
    for ref in range(size, zargs["length"]):
        turtle.setheading(ref)
        if ref % 10 == 0:
            size += 2
            turtle.pensize(size)
        turtle.forward(1)


if __name__ == "__main__":
    turtle.screensize(400, 300)
    
    turtle.ht()
    turtle.speed(0)
    turtle.delay(0)
        
    values = [
        {"length":360, "color":'red', 'size':1},
        {"length":360, "color":'green', 'size':1},
        {"length":360, "color":'blue', 'size':1},
        {"length":360, "color":'yellow', 'size':1}
        ]
    
    dots = Enumerator(len(values))
    ss = 0
    for angle in dots.next():
        draw_circle(angle, values[ss])
        ss += 1
        
    turtle.mainloop()



