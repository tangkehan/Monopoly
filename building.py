from cmu_112_graphics import *


class Building():
    def __init__(self,name, color, location, side, price):
        self.name = name
        self.location = location 
        self.color = color
        self.side = side
        self.price = price
        self.owner = None
        self.isBought = False

        