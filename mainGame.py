from cmu_112_graphics import *
from Building import *
from Chance import *
from MagicTax import *
from Corner import*
import random

def appStarted(app):
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
    app.buildings = []
    app.map = assignBuildings(app)
    app.click = None

    app.diceLocation = (app.cornerSize + app.gridHeight, app.boardSize - app.cornerSize - app.gridHeight + 20)
    app.diceImage = app.loadImage('side6.png')
    app.diceImage = app.scaleImage(app.diceImage, 0.5)
    app.rollNumber = -1

    app.playerTurn = True
    app.isGameOver = False


  

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
    red01 = Building('Sushi\nSpot', 'red', app.up[0], 'up', 140, 15)
    red02 = Building('BBQ\nPit', 'red', app.up[1], 'up', 170, 20)
    blue01 = Building('Dog\nPark', 'sky blue', app.up[2], 'up', 180, 25)
    blue02 = Building('Cat\nCafe', 'sky blue', app.up[4], 'up', 200, 30)
    
    chance04 = Chance(app.up[5])
    tax03 = MagicTax(app.up[3], 50)
 
    # initialize the left side building
    orange01 = Building('Winter\nLodge', 'orange', app.left[0], 'left', 140, 15)
    orange02 = Building('Spring\nGarden', 'orange', app.left[2], 'left', 170, 20)
    yellow01 = Building('Happy\nBash', 'gold', app.left[4], 'left', 180, 25)
    yellow02 = Building('Feast\nHall', 'gold', app.left[5], 'left', 200, 30)

    chance03 = Chance(app.left[3])
    tax02 = MagicTax(app.left[1], 100)

    # initialize the right side building
    purple01 = Building('Ocean\nView', 'Mediumpurple1', app.right[2], 'right', 110, 12)
    purple02 = Building('Beach\nResort', 'Mediumpurple1', app.right[4], 'right', 180, 20)
    purple03 = Building('Harvest\nMarket', 'Mediumpurple1', app.right[5], 'right', 140, 15)
  
    chance05 = Chance(app.right[1])
    tax04 = MagicTax(app.right[0], 100)
    tax05 = MagicTax(app.right[3], 200)


    map = [go, green01, green02, green03, chance01, tax01, chance02, 
            jail, yellow01, yellow02, chance03, orange01, tax02, orange02,
            parking, red01, red02, blue01, tax03, blue02, chance04,
            go_to_jail, tax04, chance05, purple01, tax05, purple02, purple03]
    return map

def rollDice(app):
    app.rollNumber = random.randint(1, 6)
    

def drawDice(app, canvas):

    canvas.create_image(app.diceLocation[0],app.diceLocation[1],
                         image=ImageTk.PhotoImage(app.diceImage))
   
    if app.rollNumber > 0:
        canvas.create_text(app.diceLocation[0],app.diceLocation[1],
                         text = app.rollNumber, fill='black', font='Courier 30 bold')


def mousePressed(app, event):
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

    # click the dice to roll the dice
    if ((x - app.diceLocation[0]) ** 2 + (y - app.diceLocation[1]) ** 2) ** 0.5 <= 45:
        rollDice(app)
     


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

def drawBuildingInfo(app, canvas):  
    if app.click != None:
        app.click.drawInfo(app, canvas)       


def drawBoard(app, canvas):
    # draw the board outline
    canvas.create_rectangle(app.startLocation[0], app.startLocation[1], app.boardSize, app.boardSize, 
                             outline='black', width=3)
    
    (x, y) = app.startLocation

    # draw the grids
    # from left to right
    for i in range(0, 6):
        x1 = x + i * app.gridHeight + app.cornerSize 
        x2 = x + (i + 1) * app.gridHeight + app.cornerSize 
        y2 = y + app.cornerSize
        y3 = y + 6 * app.gridHeight + app.cornerSize 
        y4 = y3 + app.cornerSize 
        canvas.create_rectangle(x1, y, x2, y2, outline='black', width=3)
        canvas.create_rectangle(x1, y3, x2, y4, outline='black', width=3)
       

    # from up to down
    for i in range(0, 6):
        newY1 = y + i * app.gridHeight + app.cornerSize 
        newY2 = newY1 + app.gridHeight
        newX1 = x + 6 * app.gridHeight + app.cornerSize 
        newX2 = newX1 + app.cornerSize
        
        canvas.create_rectangle(newX1, newY1, newX2, newY2, 
                                 outline='black', width=3)
        canvas.create_rectangle(x, newY1, x + app.cornerSize, 
                                newY2, outline='black', width=3)
        
    # draw the corner
    # up row
    canvas.create_text(x + 0.5 * app.cornerSize, y + 0.5 * app.cornerSize, 
                       text=' Free\nParking!',fill='black', font='Courier 18 bold')
    canvas.create_text(x + 1.5 * app.cornerSize + 6 * app.gridHeight, y + 0.5 * app.cornerSize,
                        text='Go to\nJail!',fill='black', font='Courier 18 bold')

    # down side row
    canvas.create_text(x + 0.5 * app.cornerSize, y + 1.5 * app.cornerSize + 6 * app.gridHeight, 
                text='Jail!',fill='black', font='Courier 18 bold')
    canvas.create_text(x + 1.5 * app.cornerSize + 6 * app.gridHeight, y + 1.5 * app.cornerSize + 6 * app.gridHeight,
                 text='Go!',fill='black', font='Courier 18 bold')
    



def redrawAll(app, canvas):
    # give the whole board a background color
    canvas.create_rectangle(0, 0, app.width, app.height, 
                            fill = '#40449b', outline='black')
    canvas.create_rectangle(app.startLocation[0], app.startLocation[1], app.boardSize, app.boardSize, 
                            fill = '#e8eefd', outline='black', width=3)
    

    drawBoard(app, canvas)
    drawDice(app, canvas)
    drawBuilding(app, canvas)
    drawBuildingInfo(app, canvas)
    


def play():
    runApp(width = 1200, height = 780)

play()

