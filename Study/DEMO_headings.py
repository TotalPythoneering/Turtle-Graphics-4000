# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-18 04:35:22
# FILE: DEMO_headings.py
# AUTHOR: Randall Nagy
# DEMO_headings.py
#
import turtle as robot

size = 1
for ref in range(360):
    robot.setheading(ref)
    if ref % 10 == 0:
        size += 2
        robot.pensize(size)
        print()
    else:
        print(".", end="")
    robot.forward(1)

robot.mainloop()

