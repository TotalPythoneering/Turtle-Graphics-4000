# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-18 07:27:30
# FILE: DEMO_world_coords.py
# AUTHOR: Randall Nagy
# DEMO_world_coords.py
#
import turtle

#turtle.setworldcoordinates(-100,-200, 400, 400)

turtle.ht()
turtle.speed(5);turtle.delay(0)
turtle.pensize(5)
for ref in range(360):
    turtle.setheading(ref)
    if ref % 10 == 0:
        print(turtle.pos())
    turtle.forward(1)

turtle.dot(100, "red")
turtle.color("green")
turtle.circle(100)

turtle.mainloop()
