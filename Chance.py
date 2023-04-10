from cmu_112_graphics import *

class Chance():
    def __init__(self, location):
        self.location = location


    def drawChance(self, canvas):
        canvas.create_text(self.location[0], self.location[1],text = "Chance",
                           fill='black', font='Courier 15')

    