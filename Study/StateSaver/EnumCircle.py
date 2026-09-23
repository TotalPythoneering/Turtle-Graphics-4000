# MISSION: Package for the Python 4000 educational opportunity.
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-4000
# DATE: 2018-07-17 13:10:06
# FILE: EnumCircle.py
# AUTHOR: Randall Nagy
#
import turtle
import StateSaver.EnumPoly as EnumPoly

'''
Parameterized Location Generator / Player
'''
class Enumerator(EnumPoly.Enumerator):

    def __init__(self, sides, degrees=360):
        super().__init__(sides)
        self.sides = sides
        self.degrees = degrees # gigo

    def next(self):
        angle = self.degrees/self.sides
        for ss in range(self.sides):
            ss += 1
            yield round(angle * ss)
        
    def enum(self, func, args):
        super().push()
        for val in self.next():
            func(val, args)
        super().pop(True)
