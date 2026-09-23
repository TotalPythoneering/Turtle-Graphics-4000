# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-17 09:45:40
# FILE: LAB_EnumPoly5.py
# AUTHOR: Randall Nagy
# LAB_EnumPoly5.py
# (Note the Tweak!)
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
    # Note: +1 gets us to that last dot!
    tweak = 1
    for ref in range(size, zargs["length"] + tweak):
        turtle.setheading(ref)
        if ref % 45 == 0:
            turtle.dot(13, '#ff0000') # AKA: 'red'
            turtle.write(
                str(int(turtle.heading())) + ":"
                + str(int(turtle.distance(0,0))) )
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



