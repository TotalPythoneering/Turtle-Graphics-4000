# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-17 10:09:04
# FILE: DEMO_Circle_Advanced.py
# AUTHOR: Randall Nagy
# DEMO_Circle_Advanced
#

import turtle

radius = 10
extent = 360    # Degrees of Completion 
steps = 3       # Divisor of Completion
for xx in range(100, 500, 100):
    for yy in range(100, 500, 100):
        print("Radius:", radius, "Extents:", extent, "Steps:", steps)
        turtle.dot(7, '#080808') # extent stop / start
        turtle.circle(radius, extent, steps)
        radius += 10
        extent -= 10
        # steps += 3
