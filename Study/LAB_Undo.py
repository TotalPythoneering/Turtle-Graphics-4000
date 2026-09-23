# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-18 09:13:48
# FILE: LAB_Undo.py
# AUTHOR: Randall Nagy
# Lab_Undo.py from LAB_EnumPoly5.py
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
    tweak = 1
    turtle.setundobuffer(1000) # Arbitrary
    for ref in range(size, zargs["length"] + tweak):
        turtle.setheading(ref)
        if ref % 45 == 0:
            turtle.dot(13, 'red')
            turtle.write(
                str(int(turtle.heading())) + ":"
                + str(int(turtle.distance(0,0))) )
        turtle.forward(1)
    ss = 0
    while turtle.undobufferentries(): # 736 / 1000
        ss += 1
        # print("Undo", ss)
        turtle.undo()


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



