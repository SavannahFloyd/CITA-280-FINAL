import pygame
class Food:

    pygame.init()
    
    def __init__(self):

        self.image = pygame.image.load('breadPiskel77.png')
        self.x = 5
        self.y = 9
        self.speed = 12
        self.size = 77

    def move(self, direction, tileMap):
        isTryMove = False
        tempX = self.x
        tempY = self.y
        if direction == "RIGHT":
            self.x = self.x + self.speed
            
            wallTestPoint1X = self.x + self.size
            wallTestPoint1Y = self.y + 5

            wallTestPoint2X = self.x + self.size
            wallTestPoint2Y = self.y + self.size - 5
            
            isTryMove = True
        elif direction == "LEFT":
            self.x = self.x - self.speed
            
            wallTestPoint1X = self.x
            wallTestPoint1Y = self.y + 5

            wallTestPoint2X = self.x
            wallTestPoint2Y = self.y + self.size - 5
            
            isTryMove = True
        elif direction == "UP":
            self.y = self.y - self.speed

            wallTestPoint1X = self.x
            wallTestPoint1Y = self.y

            wallTestPoint2X = self.x + self.size
            wallTestPoint2Y = self.y
            
            isTryMove = True
        elif direction == "DOWN":
            self.y = self.y + self.speed

            wallTestPoint1X = self.x
            wallTestPoint1Y = self.y + self.size

            wallTestPoint2X = self.x + self.size
            wallTestPoint2Y = self.y + self.size
            
            isTryMove = True
            
        if isTryMove == True:

            tiles = tileMap.getTileMap()
            tileSize = tileMap.getSpriteSize()
            wallTest1Row = (wallTestPoint1Y) // tileSize
            wallTest1Col = (wallTestPoint1X ) // tileSize

            wallTest2Row = (wallTestPoint2Y) // tileSize
            wallTest2Col = (wallTestPoint2X) // tileSize

            if not tileMap.isPassable(wallTest1Row,wallTest1Col) or not tileMap.isPassable(wallTest2Row, wallTest2Col):
                self.x = tempX
                self.y = tempY
            

        # right fridge boundary
        if self.x + self.size > 504:
            self.x = 504 - self.size
        # left fridge boundary
        if self.x < 4:
            self.x = 4
        # upper fridge boundary
        if self.y < 4:
            self.y = 4
        # lower fridge boundary
        if self.y + self.size > 604:
            self.y = 604 - self.size

                    

    def getImage(self):
        return self.image
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getSpeed(self):
        return self.speed

    def setSpeed(self, newSpeed):
        self.speed = newSpeed

    def getSize(self):
        return self.size
