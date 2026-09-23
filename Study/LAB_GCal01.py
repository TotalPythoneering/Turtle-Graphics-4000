# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-04 08:05:24
# FILE: LAB_GCal01.py
# AUTHOR: Randall Nagy
#
'''
File: LAB_GCal01.py
'''
import turtle


turtle.title("LAB_GCal01")
zfont = ("Ariel", 46, "normal")
turtle.up(); turtle.ht()

while True:
    value1 = turtle.numinput("Value One", "Enter Value:")
    if value1 is None or int(value1) is 0:
        break
    value2 = turtle.numinput("Value Two", "Enter Value:")
    if value2 is None or int(value2) is 0:
        break
    
    ops = "+-*/q"
    while True:
        op = turtle.textinput("Operand", ops)
        if op is not None and len(op.strip()) is 1:
            if op in ops:
                break

    if op is 'q':
        break
    
    turtle.clear()
    calc = str(value1) + " " + op + " " + str(value2)
    result = eval(calc)
    turtle.goto(-300, 100)
    turtle.write(calc + " = " + str(result), font=zfont)

turtle.bye()
# turtle.done()
