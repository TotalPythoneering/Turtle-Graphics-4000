# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-06 14:40:18
# FILE: DEMO_numinput.py
# AUTHOR: Randall Nagy
# ex_22_numinput
#

import turtle as robot

robot.up();robot.ht()
message = robot.Turtle()
message.up();message.ht()

# "No-Draw State"
def draw_box(color, zLen):
    robot.down()
    robot.color(color)
    for line in range(4):
        robot.forward(zLen)
        robot.left(90)
    robot.up()

pos = (0, -50)
ref = -1
while ref is not None:
    robot.home()
    ref = robot.numinput(
        'Press Cancel To Quit',
        "Rectangle Size?",
        minval=5, maxval=500,
        default=100)
    if ref is not None:
        message.clear()
        message.goto(pos)
        message.write("Size: " + str(int(ref)))
        draw_box('blue', ref)
    else:
        robot.bye()





