import pygame
from OurSprite import OurSprite
from SpriteTileMap import SpriteTileMap
pygame.init()

screen = pygame.display.set_mode((400,300))
done = False

white = pygame.image.load("C:\\Users\\Caroline\\Documents\\CofC Spring 2016\\Game Programming\\FinalGame\\white.png")
white.convert_alpha()

gray = pygame.image.load("C:\\Users\\Caroline\\Documents\\CofC Spring 2016\\Game Programming\\FinalGame\\gray.png")
gray.convert_alpha()        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

    fridgeMap = SpriteTileMap("maze.txt", "sprites.txt")
    print fridgeMap.getNumCols()
    fridgeMap.printMap()
