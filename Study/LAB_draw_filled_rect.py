# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-09 11:43:20
# FILE: LAB_draw_filled_rect.py
# AUTHOR: Randall Nagy
#
import turtle as robot

def draw_rect(pos, extents):
    robot.goto(pos)
    for line in range(2):
        robot.forward(extents[0])
        robot.left(90)
        robot.forward(extents[1])
        robot.left(90)

def draw_filled_rect(pos, extents, color=None):
    chold = robot.color()
    # robot.goto(pos)
    if color is not None:
        robot.color(color)
        robot.fillcolor(color)
        robot.begin_fill()
        
    draw_rect(pos, extents)
    
    if color is not None:
        robot.end_fill()
        robot.color(chold[0],chold[1])    


if __name__ == '__main__': 
    size = [100,100]
    draw_filled_rect((-150, 0), size, 'red')
    draw_filled_rect((0, 0), size, 'green')
    draw_filled_rect((0, 150), size, 'blue')

    robot.done()




