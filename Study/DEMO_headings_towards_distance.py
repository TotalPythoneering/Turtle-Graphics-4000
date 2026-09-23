# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-17 08:31:30
# FILE: DEMO_headings_towards_distance.py
# AUTHOR: Randall Nagy
# DEMO_headings_towards_distance.py
#

import turtle as robot

for ref in range(360):
    robot.setheading(ref)
    if ref % 36 == 0:
        print("Heading", robot.heading(),
              "\tDistance From Home:", robot.distance(0, 0))
        robot.dot(13, 'red')
        robot.write(
            str(int(robot.heading())) + ":"
            + str(int(robot.distance(0,0))) )
    robot.forward(2)

robot.mainloop()

