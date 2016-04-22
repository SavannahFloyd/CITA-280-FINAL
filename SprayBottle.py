
import pygame
import os

# it is better to have an extra variable, than an extremely long line.
img_path = os.path.join('C:\Python27', 'player.png')

class Bird(object):  # represents the bird, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load("C:\Users\Caroline\Documents\CofC Spring 2016\Game Programming\FinalGame\\SB120.png")
        # the bird's position
        self.x = 0
        self.y = 0

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        screen.blit(self.image, (self.x, self.y))


pygame.init()
screen = pygame.display.set_mode((640, 400))

bird = Bird() # create an instance
clock = pygame.time.Clock()

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    bird.handle_keys() # handle the keys

    screen.fill((255,255,255)) # fill the screen with white
    bird.draw(screen) # draw the bird to the screen
    pygame.display.update() # update the screen

    clock.tick(40)
#screen = pygame.display.set_mode((700, 700))
#done = False

#sprayBottle = pygame.image.load("C:\Users\Caroline\Documents\CofC Spring 2016\Game Programming\FinalGame\\SB120.png")
#sprayBottle.convert_alpha()

#sprayBottleWidth = 120
#sprayBottleHeight = 120

#screen.blit(sprayBottle, (0, 0))
#while not done:
    #pygame.mouse.set_visible(0)
    #mouseX, mouseY = pygame.mouse.get_pos()
    #sprayBottleX = mouseX - sprayBottleWidth/2
    #sprayBottleY = mouseY - sprayBottleHeight/2

    """For event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEMOTION:
            sprayBottle.move(sprayBottleX, sprayBottleY)
            

    pygame.display.flip()
    
#def moveSprayBottle(sprayBottleX, sprayBottleY):
    #if sprayBottleY < 0:
        #screen.move(sprayBottle, sprayBottleX, 0)
    # bottom boundary
    #if sprayBottleY + 120 > 699:
        #screen.move(sprayBottle, sprayBottleX, 579)
        

#screen.onMouseMove(moveSprayBottle)
#for event in pygame.event.get():
    #if event.type == MOUSEBUTTONDOWN:    #Remember to use: from pygame.locals import *
        #coordinates = pygame.mouse.get_pos()  
        #set x and y to respective values of coordinates
        #Enter necessary code here after"""
