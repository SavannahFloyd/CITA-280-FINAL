import pygame
class Food:

    pygame.init()
    
    def __init__(self):

        self.image = pygame.image.load('breadPiskel77.png')
        self.x = 5
        self.y = 9
        self.speed = 8
        self.size = 77

    def move(self, direction):

        if direction == "RIGHT":
            self.x = self.x + self.speed
        elif direction == "LEFT":
            self.x = self.x - self.speed
        elif direction == "UP":
            self.y = self.y - self.speed
        elif direction == "DOWN":
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
