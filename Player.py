from cmu_112_graphics import *
import random
import building

class Player:

    
    def __init__(self, name, player,  map):

        self.name = name
        # True is player, false is ai
        self.player = player
        self.map = map
        self.money = 1500
        self.index = 0
        #record the number rounds
        self.round = 0

        # the start location is go
        self.currentLocation = self.map[0].location
        self.startIndex = 0
        self.rollNum = -1
        self.isMove = False
        self.endIndex = -1

        #magic list means additional bonus
        self.magiclist=[0,4,5,6,7,10,12,14,18,20,21,22,23,25]
        self.buildings = []
    
    
    def rollDice(self):
        self.rollNum =  random.randint(1, 6)
        self.endIndex = (self.startIndex + self.rollNum) % 28
        self.index += self.rollNum
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
    
    def player_moveAStep(self, app):
        if self.isMove:
            self.startIndex += 1
            self.startIndex %= 28
            self.currentLocation = self.map[self.startIndex].location
        
        if self.startIndex == self.endIndex and self.isMove:
            app.whosTurn = 'ai'
            # print("current turn is: ", app.whosTurn)
            # print("reach here")
            self.isMove = False
            
    def getIndex(self):
        return self.index


    def ai_moveAStep(self, app):
        if self.isMove:
            self.startIndex += 1
            self.startIndex %= 28
            self.currentLocation = self.map[self.startIndex].location

        if self.startIndex == self.endIndex and self.isMove:
            app.whosTurn = 'player'
            # print("current turn is: ", app.whosTurn)
            # print("reach here")
            self.isMove = False
    
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
 
    