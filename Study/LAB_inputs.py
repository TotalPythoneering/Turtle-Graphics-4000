# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-06 06:00:24
# FILE: LAB_inputs.py
# AUTHOR: Randall Nagy
# LAB_inputs
#

import turtle as robot

robot.up();robot.ht()
message = robot.Turtle()
message.up();message.ht()


class Boxer:
    DEFAULT_COLOR = 'green'
    DEFAULT_FILL = 'yellow'
    def __init__(self, pen_size=3, box_size=100,
                 zcolor=None, zfill=None,
                 zturtle=robot.Turtle()):
        if zcolor is None:
            zcolor = Boxer.DEFAULT_COLOR
        if zfill is None:
            zfill = Boxer.DEFAULT_FILL
        self.pen_size = pen_size
        self.box_size = box_size
        self.color = zcolor
        self.fill  = zfill
        self.turtle= zturtle


def draw_box(zbox):
    if isinstance(zbox, Boxer) is False:
        zbox = Boxer()
    zbox.turtle.down()
    zbox.turtle.color(zbox.color, zbox.fill)
    zbox.turtle.begin_fill()
    zbox.turtle.width(zbox.pen_size)
    for line in range(4):
        zbox.turtle.forward(zbox.box_size)
        zbox.turtle.left(90)
    zbox.turtle.end_fill()
    zbox.turtle.up()


zbox = Boxer()
while True:  
    zbox.box_size = robot.numinput(
        'Press Cancel To Quit',
        "Rectangle Size?", default=100)
    if zbox.box_size is None:
        break
    
    zbox.pen_size = robot.numinput(
        'Press Cancel To Quit',
        "Pen Size?", default=3)
    if zbox.pen_size is None:
        break
    
    zbox.color = robot.textinput(
        'Press Cancel To Quit',
        "Pen Color?")
    if zbox.color is None:
        break
    if len(zbox.color) < 3:
        zbox.color = Boxer.DEFAULT_COLOR
    
    zbox.fill = robot.textinput(
        'Press Cancel To Quit',
        "Fill Color?")
    if zbox.fill is None:
        break
    if len(zbox.fill) < 3:
        zbox.fill = Boxer.DEFAULT_FILL
    
    draw_box(zbox)
    

robot.bye()





