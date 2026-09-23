# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-17 14:51:40
# FILE: DEMO_undo_management.py
# AUTHOR: Randall Nagy
# DEMO_undo_management.py
#
import turtle as robot

robot.setundobuffer(10)
robot.pensize(10)
robot.dot(50, "blue")
for line in range(4):
    robot.forward(100)
    robot.left(90)

while robot.undobufferentries():
    robot.undo()

robot.mainloop()

