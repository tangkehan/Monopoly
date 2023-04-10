from cmu_112_graphics import *
import building

def appStarted(app):
    app.width = 1200
    app.height = 780
    

    app.row = 8
    app.col = 8

    app.startLocation = (10, 10)

    app.connerSize = 110
    app.gridHeight = 90
    app.boardSize = 2 * app.connerSize + (app.row - 2) * app.gridHeight + app.startLocation[0]
    
    app.connor, app.up, app.down, app.left, app.right = getAllLocation(app)
    app.buildings = []
  

def getAllLocation(app):
    # get conner Locations 
    # up left [free parking, go to jail, jail, go]
    left = app.startLocation[0] + 0.5 * app.connerSize
    right = app.startLocation[0] + 1.5 * app.connerSize + 6 * app.gridHeight    
    up = app.startLocation[1] + 0.5 * app.connerSize

    # down left to right  
    down = app.startLocation[1] + 6 * app.gridHeight + 1.5 * app.connerSize
    connerLocation = [(left, up), (right, up), (left, down), (right, down)]

    upLocation = []
    downLocation = []
    for i in range(0, 6):
        x = app.startLocation[0] + (i + 0.5) * app.gridHeight + app.connerSize 
        y1 = app.startLocation[1] + 0.5 *  app.connerSize
        y2 = app.startLocation[1] + 6 * app.gridHeight + 1.5 * app.connerSize
        upLocation.append((x,y1))
        downLocation.append((x,y2))

    leftLocation = []
    rightLocation = []
    for i in range(0, 6):
        x1 = app.startLocation[0] + 0.5 *  app.connerSize
        x2 = app.startLocation[0] + 6 * app.gridHeight + 1.5 * app.connerSize
        y = app.startLocation[1] + (i + 0.5) * app.gridHeight + app.connerSize 
        leftLocation.append((x1,y))
        rightLocation.append((x2,y))

    return connerLocation, upLocation, downLocation, leftLocation, rightLocation

# test code #
# def checkAndDraw(m, canvas):
#     for (x, y) in m:
#         canvas.create_text(x,y,text='!',fill='black',font='Courier 18 bold')

# def checkDraw(app, canvas):
#     checkAndDraw(app.connor,canvas)
########################################################

# give each gird name build or something else
def assignBuildings():
    return 42



def drawBoard(app, canvas):
    # give the whole board a background color
    canvas.create_rectangle(0, 0, app.width, app.height, 
                            fill = 'sky blue', outline='white')


    (x, y) = app.startLocation
    # draw the whole board
    canvas.create_rectangle(x, y, app.boardSize, app.boardSize, 
                            fill = 'light blue', outline='black', width=3)

    # draw the buildings
    # from left to right
    for i in range(0, 6):
        x1 = x + i * app.gridHeight + app.connerSize 
        x2 = x + (i + 1) * app.gridHeight + app.connerSize 
        y2 = y + app.connerSize
        y3 = y + 6 * app.gridHeight + app.connerSize 
        y4 = y3 + app.connerSize 
        canvas.create_rectangle(x1, y, x2, y2, fill = 'light blue', outline='black', width=3)
        canvas.create_rectangle(x1, y3, x2, y4, fill = 'light blue', outline='black', width=3)
       

    # from up to down
    for i in range(0, 6):
        newY1 = y + i * app.gridHeight + app.connerSize 
        newY2 = newY1 + app.gridHeight
        newX1 = x + 6 * app.gridHeight + app.connerSize 
        newX2 = newX1 + app.connerSize
        
        canvas.create_rectangle(newX1, newY1, newX2, newY2, 
                                fill = 'light blue', outline='black', width=3)
        canvas.create_rectangle(x, newY1, x + app.connerSize, 
                                newY2, fill = 'light blue', outline='black', width=3)
        
    # draw the conner
    # up row
    canvas.create_text(x + 0.5 * app.connerSize, y + 0.5 * app.connerSize, 
                       text='Free\nParking!',fill='black', font='Courier 18 bold')
    canvas.create_text(x + 1.5 * app.connerSize + 6 * app.gridHeight, y + 0.5 * app.connerSize,
                        text='Go to\nJail!',fill='black', font='Courier 18 bold')

    # down side row
    canvas.create_text(x + 0.5 * app.connerSize, y + 1.5 * app.connerSize + 6 * app.gridHeight, 
                text='Jail!',fill='black', font='Courier 18 bold')
    canvas.create_text(x + 1.5 * app.connerSize + 6 * app.gridHeight, y + 1.5 * app.connerSize + 6 * app.gridHeight,
                 text='Go!',fill='black', font='Courier 18 bold')


# we need to mark the building side in each side 
# def drawBuiding(building, app, canvas):

#     if building.side == 'up':

#     elif building.side == 'down':

#     elif building.side == 'left':
    
#     else:
#         return 42




def drawMaps(app, canvas):
    return 42



def redrawAll(app, canvas):
    drawBoard(app, canvas)


def play():
    runApp(width = 1200, height = 780)

play()

