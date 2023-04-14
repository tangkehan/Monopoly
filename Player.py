from cmu_112_graphics import *
from entity.event import ChanceEvent
from entity.event import TaxEvent
import random



class Player:
    flag = True
    def __init__(self, name, player, map):

        self.name = name
        # True is player, false is ai
        self.player = player
        self.map = map
        

        # the start location is go
        self.currentLocation = self.map[0].location
        self.startIndex = 0
        self.rollNum = -1
        self.isMove = False
        self.endIndex = -1
        self.money = 1500
        self.in_jail = False
       
    
    def rollDice(self):
        # Shes add go_to_jail function
        # test version
        if Player.flag:
            Player.flag = False
            self.rollNum = 21 #"go_to_jail" is in 21st cell, roll number for 21 just for test
        else:
            self.rollNum =  random.randint(1, 6)
        self.endIndex = (self.startIndex + self.rollNum) % 28        
        return self.rollNum

    def moveAStep(self, app, next_turn):
        # Stuck in jail TODO: modify roll message
        if self.in_jail and self.isMove:
            self.in_jail = False
            self.isMove = False
            app.whosTurn = next_turn
            return

        if self.isMove:
            self.startIndex += 1
            self.startIndex %= 28
            self.currentLocation = self.map[self.startIndex].location

        if self.startIndex == self.endIndex and self.isMove:
            b = app.map[self.endIndex]
            if type(b).__name__ == 'Chance':
                self.chance_event()
                print(self.money)
            elif hasattr(b, 'name') and b.name == 'go to jail':
                jail, self.startIndex = self.find_jail()
                self.currentLocation = jail.location
                self.in_jail = True
            # print("current turn is: ", app.whosTurn)
            # print("reach here")
            app.whosTurn = next_turn
            self.isMove = False
    
    def find_jail(self):
        for i in range(len(self.map)):
            if hasattr(self.map[i], 'name') and self.map[i].name == 'jail':
                return self.map[i], i
            
        
        
    # XS add chance function
    # Shes change the Magic Tax and Chance to Enum
    def chance_event(self):
        self.money += random.choice(list(ChanceEvent)).value

    def tax_event(self):
        self.money += random.choice(list(TaxEvent)).value
 