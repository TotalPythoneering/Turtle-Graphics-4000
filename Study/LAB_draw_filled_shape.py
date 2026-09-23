# MISSION: The complete set of examples and source code for ''Python 4000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-09 11:42:48
# FILE: LAB_draw_filled_shape.py
# AUTHOR: Randall Nagy
#
import turtle as robot

class MyVector:
    def __init__(self, angle, length):
        self.angle = angle
        self.length = length
        

class MyShape:
    def __init__(self, vectors):
        self.vectors = vectors
        
    def draw_shape(self, pos, robot):
        robot.goto(pos)
        for line in self.vectors:
            robot.left(line.angle)
            robot.forward(line.length)
        robot.goto(pos)

    def draw_filled_shape(self, pos, robot, color=None):
        chold = robot.color()
        robot.goto(pos)
        if color is not None:
            robot.color(color)
            robot.fillcolor(color)
            robot.begin_fill()
        
        self.draw_shape(pos, robot)
        
        if color is not None:
            robot.end_fill()
            robot.color(chold[0],chold[1])    


if __name__ == '__main__': 
    vectors = list()
    for count in range(8):
        vectors.append(MyVector(10 * count, 10 * count))
    test = MyShape(vectors)
    test.draw_filled_shape((-150, 0), robot, color='red')
    test.draw_filled_shape((0, 0), robot, color='green')
    test.draw_filled_shape((0, 150), robot, color='blue')

    robot.done()




