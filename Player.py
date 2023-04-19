from cmu_112_graphics import *
from event import ChanceEvent
from event import TaxEvent
import random



class Player:
    flag = True
    def __init__(self, name, player, map):

        self.name = name
        # True is player, false is ai
        self.player = player
        self.map = map
        self.money = 1500
        #record the number rounds
        self.round = 0

        # the start location is go
        self.currentLocation = self.map[0].location
        self.index = 0
        self.startIndex = 0
        self.rollNum = -1
        self.isMove = False
        self.endIndex = -1
       
        self.in_jail = False
        
        #magic list means additional bonus
        self.magiclist=[0,4,5,6,7,10,12,14,18,20,21,22,23,25]
        self.buildings = []
    
    def rollDice(self):
        # Shes add go_to_jail function
        # test version
        if Player.flag:
            Player.flag = False
            self.rollNum = 21 #"go_to_jail" is in 21st cell, roll number for 21 just for test
        else:
            self.rollNum =  random.randint(1, 6)
        self.endIndex = (self.startIndex + self.rollNum) % 28
        
        #pw
        if self.index>27:
            self.index = self.index-27-1
            self.round +=1
            #helper function reset isRent status each turn
            for i in range(len(self.map)):
                building = self.map[i]
                if i in self.magiclist:
                    continue
                building.reset()
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

        # Shes in jail function
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


    #Peiwen :current Money
    def getCurrMoney(self):
        #show current money in the pocket
        if self.money > 0:
            return self.money
        else:
            return -1

    
    #Peiwen: buy buildings
    #give current location
    #check if bought if not: return
        #ask if you decide to buy the building 
            #yes: minus money, building list append the building
    def buyBuiding(self):
        #Peiwen: correct index every turn
        if self.index in self.magiclist:
            return
        currBuilding = self.map[self.index]
        if currBuilding.isBought == False:
            self.buildings.append(currBuilding)
            self.money -= currBuilding.price
            currBuilding.addOwner(self.name)
            currBuilding.getMessage()

    #Peiwen        
    def playerRent(self):
        if self.index in self.magiclist:
            return
        currLocation = self.map[self.index]
        if currLocation.owner == "ai":
            if currLocation.isRent == False:
                rentfee = currLocation.rentfee
                self.money -= rentfee
                currLocation.isRent = True
    
    def aiRent(self):
        if self.index in self.magiclist:
            return
        currLocation = self.map[self.index]
        if currLocation.owner == "player":
            if currLocation.isRent == False:
                rentfee = currLocation.rentfee
                self.money -= rentfee
                #lock the location in this turn, make sure rent the location only once
                currLocation.isRent = True
 