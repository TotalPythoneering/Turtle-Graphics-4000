# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-12 09:31:52
# FILE: LAB_EnumPoly1.py
# AUTHOR: Randall Nagy
#
import turtle
from StateSaver.EnumPoly import Enumerator


def do_square(angle, zargs):
    turtle.pensize(10)
    turtle.penup();turtle.goto(zargs['xcord'], zargs['ycord'])
    turtle.pendown()
    for index in range(4):
        turtle.color(zargs['color'])
        turtle.left(angle)
        turtle.forward(zargs['width'])
        
def do_dot(ignored, zargs):
    turtle.home()
    turtle.penup();turtle.goto(zargs['xcord'], zargs['ycord'])
    turtle.dot(zargs['width'], zargs['color'])


if __name__ == "__main__":
    turtle.ht()
    turtle.speed(0)
    turtle.delay(0)

    values = [
        {"xcord":100, "ycord":100, 'width':50, "color":'red'},
        {"xcord":-100, "ycord":100, 'width':50, "color":'blue'},
        {"xcord":100, "ycord":-100, 'width':100, "color":'gold'},
        {"xcord":-100, "ycord":-100, 'width':80, "color":'green'}            
        ]
    dots = Enumerator(len(values))
    func = do_dot
    # func = do_square
    for ss, angle in enumerate(dots.next()):
        func(90, values[ss])

    turtle.mainloop()



