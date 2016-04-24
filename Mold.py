from random import randint
import pygame

class Mold:

    pygame.init()
    
    def __init__(self, color):
        if color == 'blue':
            self.color = 'blue'
            self.image = pygame.image.load('bluemold50.png')
            self.speed = 10
            self.x = 0
            self.y = 0

        elif color == 'green':
            self.color = 'green'
            self.image = pygame.image.load('greenmold50.png')
            self.speed = 10
            self.x = 0
            self.y = 0
            
        self.size = 50
        self.state = "START"
        self.direction = 0
        
    #def decide(self
    def move(self):
        if self.color == 'blue':
            self.direction = randint(1,4)
        elif self.color == 'green':
            self.direction = randint(1,4)

        # left
        if self.direction == 1:
            self.x = self.x + self.speed
        # right
        elif self.direction == 2:
            self.x = self.x - self.speed
        # up
        elif self.direction == 3:
            self.y = self.y - self.speed
        # down
        elif self.direction == 4:
            self.y = self.y + self.speed

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

    def getState(self):
        return self.state

    def getImage(self):
        return self.image

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getSize(self):
        return self.size
    def setPosition(self, x, y):
        self.x,self.y = x, y
