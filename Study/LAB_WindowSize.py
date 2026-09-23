# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-06-19 16:09:26
# FILE: LAB_WindowSize.py
# AUTHOR: Randall Nagy
#
import turtle

turtle.setup(300, 100)
turtle.title("Lab_WindowSize")
print("window_width", turtle.window_width())
print("window_height", turtle.window_height())

turtle.done()

# Only shown after window closes
print("done!")

