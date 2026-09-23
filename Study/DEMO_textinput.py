# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-06 05:07:06
# FILE: DEMO_textinput.py
# AUTHOR: Randall Nagy
# Num and Text Basics
#

import turtle as robot

def draw_box(color, zLen):
    robot.color(color)
    for line in range(4):
        robot.forward(zLen)
        robot.left(90)


ref = robot.numinput('Press Cancel To Quit', "Rectangle Size?")
if ref is not None:
    color = robot.textinput('Default is "RED"', "Rectangle Color?")
    if color is None:
        color = 'red' # Default
    print(color, ref)
    draw_box(color, ref)

robot.bye()






