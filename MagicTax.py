from cmu_112_graphics import *

class MagicTax():
    def __init__(self, location, taxfee):
        self.location = location
        self.taxfee = taxfee
    
    def drawTax(self, canvas):
        canvas.create_text(self.location[0], self.location[1],text = "Magic\nTax",
                           fill='black', font='Courier 15')
