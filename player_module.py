from cmu_112_graphics import *
import random
import sys
import pygame

class Player:
    def __init__(self,name,isPlayer, loc_list:dict):
        self.name = name
        self.money = 1500
        self.isGoingToMove = False
        self.isMyTurn = True
        self.movable = True
        self.position = Position(loc_list)
        self.temp_position = False
        self.locatBuilding = 0
        self.ownBuilding = []
        self.isPlayer = isPlayer
        self.soundPlay = 0
        #Chance还需要完善一下
        self.chance = 0
        #self.showText = []

    #这个方法用来确定玩家（self）的位置
    def getPosition(self, buildings):
        for building in buildings:
            for position in building.location:
                if self.position == position:
                    return building
        return None
    
    #玩家按y购买房子
    def buyBuilding(self,isPressYes):
        if self.locatBuilding.owner != self.name:
            if isPressYes:
                self.locatBuilding.owner = self.name
                self.locatBuilding.isBought = True
                self.ownBuilding.append(self.locatBuilding)
                self.money = self.money - 50
                #我们的例子用的是self.showText = [self.name + "bought" + self.locatBuilding.name]
                print(f"{self.name} bought {self.locatBuilding.name}")
                self.soundPlay = 0 #音效这里得修改
                return True
            else:
                return False
        else:
            return "You have owned this building ！"


    def move_player(self, value:int):
        self.position.move(value)
    
    def eventInPosition(self,allplayers):
        building = self.locatBuilding
        if building.name!='free parking' and building.name!='go to jail' and building.name!='jail'\
        and building.name!='go' and building.name!='go to jail':
            if self.locatBuilding.isBought == False:
                if self.isPlayer == True:
                    print("Please roll the dice")
                else:
                    print("It's not your turn")
            else:
                print("This land has been occupied")
        else:
            print("This land cannot be bought")


class Position:
    def __init__(self, loc_lst:dict):
        self.data = 0 # from 0 to 27
        self.loc_lst = loc_lst
        self.location = []
        self.convertToLocation()

    def convertToLocation(self):
        location_int = self.data // 7
        location_rem = self.data % 7
        if location_rem == 0:
            location_name = 'corner'
            # go = Corner('go', app.corner[3]) --> Position: 0
            # jail = Corner('jail', app.corner[2]) --> Position: 6
            # parking = Corner('free parking', app.corner[0]) --> Position: 13
            # go_to_jail = Corner('go to jail', app.corner[1]) --> Position: 20
            corner_order = [3, 2, 0, 1]
            location_index = corner_order[location_int]   
        else:
            if location_int == 0:
                location_name = 'down'
                location_index = 6 - location_rem
            elif location_int == 1:
                location_name = 'left'
                location_index = 6 - location_rem
            elif location_int == 2:
                location_name = 'up'
                location_index = location_rem - 1
            else:
                location_name = 'right'
                location_index = location_rem - 1
        # print(location_name,location_index)
        # print(self.loc_lst)
        # print(self.data)
        self.location = self.loc_lst[location_name][location_index]

    

    def move(self, value:int):
        self.data += value
        self.data %= 28
        self.convertToLocation()