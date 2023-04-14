from cmu_112_graphics import *
import random


class Player:
    def __init__(self, name, player,  map):

        self.name = name
        # True is player, false is ai
        self.player = player
        self.map = map
        self.money = 1500

        # the start location is go
        self.currentLocation = self.map[0].location
        self.startIndex = 0
        self.rollNum = -1
        self.isMove = False
        self.endIndex = -1
       
    
    def rollDice(self):
        self.rollNum =  random.randint(1, 6)
        self.endIndex = (self.startIndex + self.rollNum) % 28
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
    #check if bought if not: 弹窗
        #ask if you decide to buy the building 
            #yes: 减钱、building list append the building



    

 