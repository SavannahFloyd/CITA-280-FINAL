import pygame
class SprayBottle:

    pygame.init()
    
    def __init__(self):

        self.image = pygame.image.load('SB70.png')
        self.x = 0
        self.y = 0
        self.size = 70
        
    def move(self, mouseX, mouseY):
        
        self.x = mouseX - self.size/2
        self.y = mouseY - self.size/2

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
    def getSize(self):
        return self.size
        
        
