# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-19 08:25:42
# FILE: LAB_EnumPoly6.py
# AUTHOR: Randall Nagy
# LAB_EnumPoly6.py
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
    for ref in range(size, zargs["length"] + tweak):
        turtle.setheading(ref)
        if ref % 45 == 0:
            turtle.dot(13, 'red')
            turtle.write(
                str(int(turtle.heading())) + ":"
                + str(int(turtle.distance(0,0))) )
        turtle.forward(1)


if __name__ == "__main__":
    dime = (400, 300)
    turtle.screensize(dime[0], dime[1])
    turtle.setup(dime[0],dime[1], 500,250) # New - Screen Location
    turtle.setworldcoordinates(-dime[0]/2, -dime[1]/2, dime[0]/2, dime[1]/2)
    
    turtle.ht()
    turtle.speed(0)
    turtle.delay(0)
      
    values = [
        {"length":360, "color":'red', 'size':1},
        {"length":360, "color":'green', 'size':1},
        {"length":360, "color":'blue', 'size':1},
        {"length":360, "color":'yellow', 'size':1}
        ]
    
    skews = [
        {"ll":-dime[0], "lr":-dime[1], "ul":dime[0], "ur":dime[1]},
        {"ll":-dime[0]/2, "lr":-dime[1], "ul":dime[0], "ur":dime[1]},
        {"ll":-dime[0], "lr":-dime[1]/2, "ul":dime[0], "ur":dime[1]},
        {"ll":-dime[0], "lr":-dime[1]*4, "ul":dime[0], "ur":dime[1]},
        ]

    dots = Enumerator(len(values))
    ss = 0
    for angle in dots.next():
        draw_circle(angle, values[ss])
        turtle.setworldcoordinates(skews[ss]['ll'], skews[ss]['lr'],
                                   skews[ss]['ul'], skews[ss]['ur'])
        import time
        time.sleep(2)
        ss += 1
        
    turtle.mainloop()



