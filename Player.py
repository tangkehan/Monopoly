from cmu_112_graphics import *
import random


class Player:
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
         
        


    # XS add chance function
    def chance_event(app, player_money, computer_money):
        penalties = {
            "Mining tax": 100,
            "toxic emissions": 150,
            "Deforestation": 200,
            "Overfishing": 100,
            "Fire damage": 250
        }

        rewards = {
            "Recycle": 200,
            "plant trees": 150,
            "Zero Waste": 150,
            "Save Bees": 100,
            "Reduce Plastic": 250,
            "Educate public": 250
        }

        selected_chance = random.choice(list(penalties.keys()) + list(rewards.keys()))
        if selected_chance in penalties:
            # app.drawChanceRewards()
            amount = penalties[selected_chance]
        else:
            # app.drawChancePenalty()
            amount = rewards[selected_chance]

        player_money -= amount
        computer_money += amount

        return player_money, computer_money
          


 