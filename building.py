from cmu_112_graphics import *


class Building():
    def __init__(self, name, color, location, side, price, rent):
        self.name = name
        # center location
        self.location = location 
        self.color = color
        # up// down // left // right
        self.side = side
        self.price = price
        self.owner = None
        self.rentfee = rent
        self.isBought = False

        
    def getMessage(self):
        if self.owner == None:
            return 'Don not have owner yet!'
        else:
            return self.owner


    def getColorLocation(self, app):
        (x, y) = self.location
        x1, x2, y1, y2 = 0, 0, 0, 0
        if self.side == 'up':
            x1 = x - 0.5 * app.gridHeight
            x2 = x + 0.5 * app.gridHeight

            y2 = y + 0.5 * app.cornerSize
            y1 = y2 - 20

        if self.side == 'down':
            x1 = x - 0.5 * app.gridHeight
            x2 = x + 0.5 * app.gridHeight

            y1 = y - 0.5 * app.cornerSize
            y2 = y1 + 20

        if self.side == 'left':
            y1 = y - 0.5 * app.gridHeight
            y2 = y + 0.5 * app.gridHeight

            x1 = x + 0.5 * app.cornerSize
            x2 = x1 - 20

        if self.side == 'right':
            y1 = y - 0.5 * app.gridHeight
            y2 = y + 0.5 * app.gridHeight

            x1 = x - 0.5 * app.cornerSize
            x2 = x1 + 20

        return x1, y1, x2, y2
    
    def getOwnerLocation(self, app):
        (x, y) = self.location
        x1, x2, y1, y2 = 0, 0, 0, 0
        if self.side == 'up':
            x1 = x - 0.5 * app.gridHeight
            x2 = x + 0.5 * app.gridHeight

            y1 = y - 0.5 * app.cornerSize
            y2 = y1 + 20

        if self.side == 'down':
            x1 = x - 0.5 * app.gridHeight
            x2 = x + 0.5 * app.gridHeight

            y1 = y + 0.5 * app.cornerSize
            y2 = y1 - 20

        if self.side == 'left':
            y1 = y - 0.5 * app.gridHeight
            y2 = y + 0.5 * app.gridHeight

            x1 = x - 0.5 * app.cornerSize
            x2 = x1 + 20

        if self.side == 'right':
            y1 = y - 0.5 * app.gridHeight
            y2 = y + 0.5 * app.gridHeight

            x1 = x + 0.5 * app.cornerSize
            x2 = x1 - 20

        return x1, y1, x2, y2
    
    def getWholeLocation(self, app):
        (x, y) = self.location
        if self.side == 'up' or self.side == 'down':
            x1 = x - 0.5 * app.gridHeight
            x2 = x + 0.5 * app.gridHeight
            y1 = y - 0.5 * app.cornerSize
            y2 = y + 0.5 * app.cornerSize

        if self.side == 'left' or self.side == 'right':
            x1 = x - 0.5 * app.cornerSize
            x2 = x + 0.5 * app.cornerSize
            y1 = y - 0.5 * app.gridHeight
            y2 = y + 0.5 * app.gridHeight
        
        return x1, y1, x2, y2

    
    # XS : changed width to 1 
    def drawColorAndName(self, app, canvas):
        x1, y1, x2, y2 = self.getColorLocation(app)
        canvas.create_rectangle(x1, y1, x2, y2,
                            fill = self.color, outline='black', width = '1')
        canvas.create_text(self.location[0], self.location[1],text = self.name,
                           fill='black', font='Courier 13')  # XS font-size

    def drawOwner(self, app, canvas):
        x1, y1, x2, y2 = self.getOwnerLocation(app)
        if self.owner == 'player':
            canvas.create_rectangle(x1, y1, x2, y2,
                                fill = 'snow' , outline='black', width = '1')
        if self.owner == 'AI':
            canvas.create_rectangle(x1, y1, x2, y2,
                                fill = 'black' , outline='black', width = '1')
    # XS changed the coordinate        
    def drawInfo(self, app, canvas):
        x1 = app.boardSize + 30
        x2 = app.width - 70
        canvas.create_rectangle(x1, 0.5 * app.height, x2, 0.5 * app.height + 340,
                              fill = '#e8eefd', outline='black', width=0)
        
        # small rectangle
        canvas.create_rectangle(x1, 0.5 * app.height, x2, 0.5 * app.height + 100,
                             fill = self.color, outline='black', width=0)
       
        canvas.create_text((x1 + x2) / 2, (app.height + 100) / 2, 
                           text= self.name ,fill='Black', font='Courier 15 bold')  # XS font-size
        
        # canvas.create_rectangle(x1, 0.5 * app.height, x2, 1100,
        #                      outline='black', width=3)
        
        m = self.getMessage()
        canvas.create_text((x1 + x2) / 2, 0.5 * app.height + 150,
                             text= f'Rent: ${self.rentfee}\nCost of Building: ${self.price}\nOwner: {m}',
                             anchor='n',fill='black', font='Courier 12 bold') 
        
    

        
        
        








        