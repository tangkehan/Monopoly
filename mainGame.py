from cmu_112_graphics import *
from building import *
from Chance import *
from MagicTax import *
from Corner import*
import random
from player import*
import time


# import pygame
import sys

from PIL import ImageFilter  # XS
from PIL import ImageTk  # XS
from PIL import Image  # XS get button size 


############################### start page from here #############################
def startInf(app):
    app.startMessage = 'Click the buttom to enter your name!'
    app.enterNameButtonLocation = (50, 50)
    app.themeImage = Image.open('resource/theme.png')
    app.startButtonLocation = (app.width/2, app.height/2)
    app.startUpImage = app.loadImage('resource/startUp.png')
    app.startUpImage = app.scaleImage(app.startUpImage, 0.06).filter(ImageFilter.SMOOTH)
    # app.startDownImage = app.loadImage('resource/startDown.png')
    # app.startDownImage = app.scaleImage(app.startDownImage, 0.08).filter(ImageFilter.SMOOTH)
    app.playButtonLocation = [app.width/2 - 50, app.height/2 + 50]
    app.name = None


# Kehan : add the start mode mouse press and add the name part
def startMode_mousePressed(app, event):
    x, y = event.x, event.y
    x1 = app.playButtonLocation[0] - 65
    x2 = app.playButtonLocation[0] + 65
    y1 = app.playButtonLocation[1] - 30
    y2 = app.playButtonLocation[1] + 40
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
        app.mode = 'gameMode'

    (x, y) = app.enterNameButtonLocation
    d1 = ((x - event.x)**2 + (y - event.y)** 2) ** 0.5
    if d1 <= 15:
        name = app.getUserInput('What is your name?')
        app.name = name

        if (name == None):
            app.startMessage  = 'You canceled!'
                    
        else:
            app.showMessage('You entered: ' + name)
            app.startMessage  = f'Hi, {name}!'


# Kehan : startMode drawing may need change some image/color
def startMode_redrawAll(app, canvas):
    # XS: add a theme page, including the "Play(start game) button"
    # draw the cover
    canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.themeImage))

    # draw the start button
    canvas.create_image(app.playButtonLocation[0], app.playButtonLocation[1], image=ImageTk.PhotoImage(app.startUpImage))
   
    # draw the enter name button
    canvas.create_oval(app.enterNameButtonLocation[0] - 15,app.enterNameButtonLocation[1] - 15,
                       app.enterNameButtonLocation[0] + 15, app.enterNameButtonLocation[1] + 15,
                       fill = 'snow', outline = 'black')
    
    canvas.create_text(75, 50, anchor = 'w',
                       text= app.startMessage , font='Courier 20 bold', fill='white')




############################### game page from here #############################
# Kehan: gameInf is to store some global parameters

def gameInf(app):
    app.width = 1200
    app.height = 780
    
    app.row = 8
    app.col = 8

    app.startLocation = (10, 10)

    # corner size 110 * 110
    app.cornerSize = 110
    # gird size 90 * 110
    app.gridHeight = 90
    app.boardSize = 2 * app.cornerSize + (app.row - 2) * app.gridHeight + app.startLocation[0]
    
    app.corner, app.up, app.down, app.left, app.right = getAllLocation(app)
    app.loc_lst = {
        'corner': app.corner,
        'up': app.up,
        'down': app.down,
        'right': app.right,
        'left': app.left
    }
    app.buildings = []
    app.map = assignBuildings(app)
    app.click = None

    app.diceLocation = (app.cornerSize + app.gridHeight, app.boardSize - app.cornerSize - app.gridHeight + 20)
    app.diceImage = app.loadImage('side6.png')
    app.diceImage = app.scaleImage(app.diceImage, 0.6)
    app.rollNumber = -1

    # XS: draw screen needs 3 steps : load, draw, call
    # 1st: load Roll, yes, no button
    app.rollLocation = (app.cornerSize + 5 * app.gridHeight, app.boardSize - app.cornerSize - app.gridHeight + 20)
    app.rollImage = app.loadImage('resource/Roll.png')
    app.rollImage = app.scaleImage(app.rollImage, 0.02).filter(ImageFilter.SMOOTH)

    # Kehan: add round finish button
    app.finishButton = (app.rollLocation[0],  app.rollLocation[1] - 70)
    
    # Shes load Player image
    app.playerImage = app.loadImage('resource/player.png')
    app.playerImage = app.scaleImage(app.playerImage, 0.02).filter(ImageFilter.SMOOTH)
    app.playerAiImage = app.loadImage('resource/com.png')
    app.playerAiImage = app.scaleImage(app.playerAiImage, 0.02).filter(ImageFilter.SMOOTH)


    app.yesLocation = (2 * app.cornerSize + 6 * app.gridHeight + 120, app.boardSize - 80)
    app.yesImage = app.loadImage('resource/YES.png')
    app.yesImage = app.scaleImage(app.yesImage, 0.2).filter(ImageFilter.SMOOTH)

    app.noLocation = (2 * app.cornerSize + 6 * app.gridHeight + 300, app.boardSize - 80)
    app.noImage = app.loadImage('resource/NO.png')
    app.noImage = app.scaleImage(app.noImage, 0.2).filter(ImageFilter.SMOOTH)

    # XS load money_player, money_computer button 
    app.moneyPlayerLocation = (2 * app.cornerSize + 7 * app.gridHeight + 100, 1.3 * app.gridHeight)
    app.moneyPlayerImage = app.loadImage('resource/money_player.png')
    app.moneyPlayerImage = app.scaleImage(app.moneyPlayerImage, 0.8).filter(ImageFilter.SMOOTH)

    app.moneyComLocation = (2 * app.cornerSize + 7 * app.gridHeight + 100, 250)
    app.moneyComImage = app.loadImage('resource/money_com.png')
    app.moneyComImage = app.scaleImage(app.moneyComImage, 0.8).filter(ImageFilter.SMOOTH)


    # XS load price button image
    app.priceLocation = (2 * app.cornerSize + 6 * app.gridHeight + 320, app.cornerSize + 2.75 * app.gridHeight)
    app.priceImage = app.loadImage('resource/Price.png')
    app.priceImage = app.scaleImage(app.priceImage, 0.4).filter(ImageFilter.SMOOTH)


    # XS load board icon image
    app.jailImage = app.loadImage('resource/Jail.png')
    app.jailImage = app.scaleImage(app.jailImage, 0.3).filter(ImageFilter.SMOOTH)
    app.goToJailImage = app.loadImage('resource/go to jail.png')
    app.goToJailImage = app.scaleImage(app.goToJailImage, 0.6).filter(ImageFilter.SMOOTH)
    app.parkingImage = app.loadImage('resource/free parking.png')
    app.parkingImage = app.scaleImage(app.parkingImage, 0.3).filter(ImageFilter.SMOOTH)
    app.goImage = app.loadImage('resource/GO.png')
    app.goImage = app.scaleImage(app.goImage, 0.2).filter(ImageFilter.SMOOTH)

    app.taxImage = app.loadImage('resource/Tax.png')
    app.taxImage = app.scaleImage(app.taxImage, 0.3).filter(ImageFilter.SMOOTH)

    app.exitLocation = (app.width - 30, app.height - 30)
    app.exitImage = app.loadImage('resource/exit.png')
    app.exitImage = app.scaleImage(app.exitImage, 0.2).filter(ImageFilter.SMOOTH)

   

    # x, y = app.width/2 - 50, app.height/2 + 50
    # app.startButtonRect = pygame.Rect(x, y, app.startUpImage.width, app.startUpImage.height)
    # app.startButtonClicked = False


    app.playerTurn = True
    app.isGameOver = False


  
# XS 2 step:  draw Roll, yes, no button
def drawRoll(app, canvas):

    canvas.create_image(app.rollLocation[0],app.rollLocation[1],
                         image=ImageTk.PhotoImage(app.rollImage))
    
def drawFinish(app, canvas):
    canvas.create_rectangle(app.finishButton[0] - 50, app.finishButton[1] - 25,
                            app.finishButton[0] + 50, app.finishButton[1] + 25,
                         outline = 'black')
    canvas.create_text(app.finishButton[0], app.finishButton[1], text = 'Finish!',
                       fill='#1459ff', font='Courier 20 bold')
                     
    

  
def drawYesNo(app, canvas):

    canvas.create_image(app.yesLocation[0],app.yesLocation[1],
                         image=ImageTk.PhotoImage(app.yesImage))
    
    canvas.create_image(app.noLocation[0],app.noLocation[1],
                         image=ImageTk.PhotoImage(app.noImage))
    
def drawExit(app, canvas):

    canvas.create_image(app.exitLocation[0], app.exitLocation[1],
                        image=ImageTk.PhotoImage(app.exitImage))
    
    canvas.create_text(app.exitLocation[0] - 45, app.exitLocation[1], 
                       text = 'EXIT', font='Courier 12 bold', fill = 'white')

# Kehan: add the player name and computer name， Need to add more detail later
# XS draw two money button  
def drawMoney(app, canvas):
    canvas.create_image(app.moneyPlayerLocation[0],app.moneyPlayerLocation[1],
                         image=ImageTk.PhotoImage(app.moneyPlayerImage))
    canvas.create_text(app.moneyPlayerLocation[0], app.moneyPlayerLocation[1] - 40, 
                       text = app.name, font='Courier 12 bold', fill = '#88f2c4')
    canvas.create_image(app.moneyComLocation[0],app.moneyComLocation[1],
                         image=ImageTk.PhotoImage(app.moneyComImage))
    canvas.create_text(app.moneyComLocation[0],app.moneyComLocation[1] - 40, 
                       text = 'Computer', font='Courier 12 bold', fill = '#e8cffb')

def drawPrice(app, canvas):

    canvas.create_image(app.priceLocation[0],app.priceLocation[1],
                         image=ImageTk.PhotoImage(app.priceImage))

# XS draw background
def drawBackground(app, canvas):
    backgroundImage = Image.open('resource/background.png')
    backgroundPhoto = ImageTk.PhotoImage(backgroundImage)
    canvas.create_image(0, 0, anchor="nw", image=backgroundPhoto)
    canvas.lower("all")


def getAllLocation(app):
    # get corner Locations 
    # up left [free parking, go to jail, jail, go]
    left = app.startLocation[0] + 0.5 * app.cornerSize
    right = app.startLocation[0] + 1.5 * app.cornerSize + 6 * app.gridHeight    
    up = app.startLocation[1] + 0.5 * app.cornerSize

    # down left to right  
    down = app.startLocation[1] + 6 * app.gridHeight + 1.5 * app.cornerSize
    cornerLocation = [(left, up), (right, up), (left, down), (right, down)]

    upLocation = []
    downLocation = []
    for i in range(0, 6):
        x = app.startLocation[0] + (i + 0.5) * app.gridHeight + app.cornerSize 
        y1 = app.startLocation[1] + 0.5 *  app.cornerSize
        y2 = app.startLocation[1] + 6 * app.gridHeight + 1.5 * app.cornerSize
        upLocation.append((x,y1))
        downLocation.append((x,y2))

    leftLocation = []
    rightLocation = []
    for i in range(0, 6):
        x1 = app.startLocation[0] + 0.5 *  app.cornerSize
        x2 = app.startLocation[0] + 6 * app.gridHeight + 1.5 * app.cornerSize
        y = app.startLocation[1] + (i + 0.5) * app.gridHeight + app.cornerSize 
        leftLocation.append((x1,y))
        rightLocation.append((x2,y))

    return cornerLocation, upLocation, downLocation, leftLocation, rightLocation

# test code #
# def checkAndDraw(m, canvas):
#     for (x, y) in m:
#         canvas.create_text(x,y,text='!',fill='black',font='Courier 18 bold')

# def checkDraw(app, canvas):
#     checkAndDraw(app.connor,canvas)
########################################################


def assignBuildings(app):
    # initialize the corner building
    # up left [free parking, go to jail, jail, go]
    parking = Corner('free parking', app.corner[0])
    go_to_jail = Corner('go to jail', app.corner[1])
    jail = Corner('jail', app.corner[2])    
    go = Corner('go', app.corner[3])


    # initialize the down side building 
    green01 = Building('Sweet\nBakery', 'green yellow', app.down[-1], 'down', 150, 20)
    green02 = Building('Fruit\nStand', 'green yellow', app.down[-2], 'down', 180, 25)
    green03 = Building('Donkin\nDonut', 'green yellow', app.down[-3], 'down', 160, 18)
  

    chance01 = Chance(app.down[0])
    tax01 = MagicTax(app.down[1], 100)
    chance02 = Chance(app.down[2])


    # initialize the up side building
    red01 = Building('Sushi\nSpot', '#AF3800', app.up[0], 'up', 140, 15)
    red02 = Building('BBQ\nPit', '#AF3800', app.up[1], 'up', 170, 20)
    blue01 = Building('Dog\nPark', '#a5d6f7', app.up[2], 'up', 180, 25)
    blue02 = Building('Cat\nCafe', '#a5d6f7', app.up[4], 'up', 200, 30)
    
    chance04 = Chance(app.up[5])
    tax03 = MagicTax(app.up[3], 50)
 
    # initialize the left side building
    orange01 = Building('Winter\nLodge', '#f98810', app.left[0], 'left', 140, 15)
    orange02 = Building('Spring\nGarden', '#f98810', app.left[2], 'left', 170, 20)
    yellow01 = Building('Happy\nBash', '#ffdf00', app.left[4], 'left', 180, 25)
    yellow02 = Building('Feast\nHall', '#ffdf00', app.left[5], 'left', 200, 30)

    chance03 = Chance(app.left[3])
    tax02 = MagicTax(app.left[1], 100)

    # initialize the right side building
    purple01 = Building('Ocean\nView', '#4386fb', app.right[2], 'right', 110, 12)
    purple02 = Building('Beach\nResort', '#4386fb', app.right[4], 'right', 180, 20)
    purple03 = Building('Harvest\nMarket', '#4386fb', app.right[5], 'right', 140, 15)
  
    chance05 = Chance(app.right[1])
    tax04 = MagicTax(app.right[0], 100)
    tax05 = MagicTax(app.right[3], 200)


    map = [go, green01, green02, green03, chance02, tax01, chance01, 
            jail, yellow02, yellow01, chance03, orange02, tax02, orange01,
            parking, red01, red02, blue01, tax03, blue02, chance04,
            go_to_jail, tax04, chance05, purple01, tax05, purple02, purple03]
    return map
    


    
# Shes
def initPlayers(app):
    app.timerDelay = 500
    app.whosTurn = 'player'

    app.player = Player(app.name, True,  app.map)
    app.playerLocation = app.player.currentLocation
    
    app.ai = Player('ai', False, app.map)
    app.aiLocation = app.ai.currentLocation    
 



#  timerFired 里是枚0.5秒重画一切所有
# 在这里进行买房 被收租的操作，感觉可以写在move a step里面
# 当走到最后一步的时候， 查看building type, 如果买了地，
# 则需要把地的下半截涂颜色，在building里已经写好了d rawOwner(self, app, canvas)

def gameMode_timerFired(app):
    if app.whosTurn == 'player':
        app.player.player_moveAStep(app)
   
    if app.whosTurn == 'ai':
        app.ai.ai_moveAStep(app)

 
  
# Shes:
def drawPlayer(app, canvas):
    offset = 20
    float_mid_id = 1 / 2.0
    offset_value = (0 - float_mid_id) * offset
    canvas.create_image(app.player.currentLocation[0] + offset_value, app.player.currentLocation[1], 
                                    image=ImageTk.PhotoImage(app.playerImage))
    
def drawAi(app, canvas):
    offset = 20
    float_mid_id = 1 / 2.0
    offset_value = (1 - float_mid_id) * offset
    canvas.create_image(app.ai.currentLocation[0] + offset_value, app.ai.currentLocation[1], 
                                    image=ImageTk.PhotoImage(app.playerAiImage))


def gameMode_mousePressed(app, event):
    x = event.x
    y = event.y

    # click every building grid to see more information
    for i in range(len(app.map)):
        if type(app.map[i]).__name__ == 'Building':
            b = app.map[i]
            x1, y1, x2, y2 = b.getWholeLocation(app)
            if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                app.click = b
            else:
                continue
        continue


    # XS changed : click the "Roll" to roll the dice
    # Kehan : if is playe's turn , click the dice to roll
    if ((x - app.rollLocation[0]) ** 2 + (y - app.rollLocation[1]) ** 2) ** 0.5 <= 45:
        if app.whosTurn == 'player' and app.player.isMove == False:
            app.rollNumber = app.player.rollDice()
            app.noticeMessage = f" You got {app.rollNumber} !"
            app.player.isMove = True

      
    # Kehan: afrer the player click the finish button , it's computer's turn
    if(x >= app.finishButton[0] - 50 and x <= app.finishButton[0] + 50 and 
       y >= app.finishButton[1] - 25 and y <= app.finishButton[1] + 25):
        if app.whosTurn == 'ai' and  app.ai.isMove == False:
            app.rollNumber = app.ai.rollDice()
            app.noticeMessage = f" Computer got {app.rollNumber} !"  
            app.ai.isMove = True


    
    x1 = app.exitLocation[0] - 65
    x2 = app.exitLocation[0] + 65
    y1 = app.exitLocation[1] - 30
    y2 = app.exitLocation[1] + 40
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
        app.mode = 'startMode'
     

# Kehan: add the notice message
def drawDice(app, canvas):
    canvas.create_image(app.diceLocation[0],app.diceLocation[1],
                         image=ImageTk.PhotoImage(app.diceImage))
   
    if app.rollNumber > 0:
        canvas.create_text(app.diceLocation[0],app.diceLocation[1] - 25,
                         text = app.rollNumber, fill='#1459ff', font='Courier 30 bold')
        if app.noticeMessage != None:
            canvas.create_text(app.diceLocation[0], app.diceLocation[1] + 50, 
                              text = app.noticeMessage, fill='#1459ff', font='Courier 15 bold' )




def drawBuilding(app,canvas):
    for i in range(len(app.map)):
        b = app.map[i]
        if type(b).__name__ == 'Chance':
            b.drawChance(canvas)
        elif type(b).__name__ == 'MagicTax':
            b.drawTax(canvas)
        elif type(b).__name__ == 'Building':
            b.drawColorAndName(app, canvas)
        else: 
            continue


#Kehan : edit the drawing building info when click the building,
# show the detail of the building and ask if player wants to buy?
# after adding the player loop the map, need to change this part
def drawBuildingInfo(app, canvas):  
    if app.click != None:
        app.click.drawInfo(app, canvas)   
        drawYesNo(app, canvas)    


# XS : changed the outline and width
def drawBoard(app, canvas):
    # XS: draw background color of the board
    canvas.create_rectangle(app.startLocation[0], app.startLocation[1], 
                            app.boardSize, app.boardSize,  fill='#e8eefd')


    # draw the board outline
    canvas.create_rectangle(app.startLocation[0], app.startLocation[1], app.boardSize, app.boardSize, 
                             outline='black', width=1)
    
    (x, y) = app.startLocation

    # draw the grids
    # from left to right
    for i in range(0, 6):
        x1 = x + i * app.gridHeight + app.cornerSize 
        x2 = x + (i + 1) * app.gridHeight + app.cornerSize 
        y2 = y + app.cornerSize
        y3 = y + 6 * app.gridHeight + app.cornerSize 
        y4 = y3 + app.cornerSize 
        canvas.create_rectangle(x1, y, x2, y2, outline='black', width=1)
        canvas.create_rectangle(x1, y3, x2, y4, outline='black', width=1)
       

    # from up to down
    for i in range(0, 6):
        newY1 = y + i * app.gridHeight + app.cornerSize 
        newY2 = newY1 + app.gridHeight
        newX1 = x + 6 * app.gridHeight + app.cornerSize 
        newX2 = newX1 + app.cornerSize
        
        canvas.create_rectangle(newX1, newY1, newX2, newY2, 
                                 outline='black', width=1)
        canvas.create_rectangle(x, newY1, x + app.cornerSize, 
                                newY2, outline='black', width=1)
        
    # draw the corner
    # up row
    # XS Changed coordinate, font size : 10
    canvas.create_text(x + 0.4 * app.cornerSize, y + 0.2 * app.cornerSize, 
                       text=' Free\n Parking!',fill='black', font='Courier 12 bold')  
    canvas.create_text(x + 1.3 * app.cornerSize + 6 * app.gridHeight, y + 0.2 * app.cornerSize,
                        text='Go to\nJail!',fill='black', font='Courier 12 bold')

    # down side row
    canvas.create_text(x + 0.4 * app.cornerSize, y + 1.2 * app.cornerSize + 6 * app.gridHeight, 
                text='Jail!',fill='black', font='Courier 12 bold')
    # canvas.create_text(x + 1.3 * app.cornerSize + 6 * app.gridHeight, y + 1.3 * app.cornerSize + 6 * app.gridHeight,
    #              text='Go!',fill='black', font='Courier 18 bold')
    
    # XS: draw parking, gotoJail, Jail, Go icon
    canvas.create_image(x + 0.6 * app.cornerSize, y + 0.6 * app.cornerSize, 
                        image=ImageTk.PhotoImage(app.parkingImage))
    canvas.create_image(x + 1.5 * app.cornerSize + 6 * app.gridHeight, y + 0.6 * app.cornerSize,
                        image=ImageTk.PhotoImage(app.goToJailImage))
    canvas.create_image(x + 0.6 * app.cornerSize, y + 1.6 * app.cornerSize + 6 * app.gridHeight,
                        image=ImageTk.PhotoImage(app.jailImage))
    canvas.create_image(x + 1.5 * app.cornerSize + 6 * app.gridHeight, y + 1.5 * app.cornerSize + 6 * app.gridHeight,
                        image=ImageTk.PhotoImage(app.goImage))


    
# XS :
# If the game does not start, the screen shows the theme cover
# If you click "play", the game will start and the game interface will be displayed
def gameMode_redrawAll(app, canvas):


    canvas.create_rectangle(0, 0, app.width, app.height, 
                            fill = '#40449b', outline='black')
    canvas.create_rectangle(app.startLocation[0], app.startLocation[1], app.boardSize, app.boardSize, 
                            fill = '#e8eefd', outline='black', width=1)
            
    
    drawBackground(app, canvas)  # XS
    drawBoard(app, canvas)
    drawDice(app, canvas)
    drawRoll(app, canvas)   # XS
    drawBuilding(app, canvas)
    drawBuildingInfo(app, canvas)
    drawMoney(app, canvas)  # XS
    drawPrice(app, canvas)  # XS
    drawExit(app, canvas)   # XS
    drawPlayer(app, canvas) # Shes
    drawAi(app, canvas) # Kehan
    drawFinish(app, canvas) #Kehan
    


# The whole game running start here
def appStarted(app):
    app.mode = 'startMode'

    startInf(app)
    gameInf(app)
    initPlayers(app)



def play():
    runApp(width = 1200, height = 780)

play()


