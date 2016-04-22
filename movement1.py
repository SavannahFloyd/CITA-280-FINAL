import pygame
##from pygame.local import *
import sys
##from timer import timer

pygame. init()

white = (255, 255, 255)
black = (0, 0, 0)
bg = black

displayWidth = 700
displayHeight = 800
cellSize = 10

LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'
fps = 20

def gameMovement():
    startx = 0
    starty = 0
    coords = [{'x': startx, 'y': starty}]
    done = False
    direction = RIGHT

    isAlive = 'yes'

    while done == False: #or if timer > 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    direction = DOWN
                    ##done = False

                elif event.key == pygame.K_UP:
                    direction = UP
                    ##done = False

                elif event.key == pygame.K_LEFT:
                    direction = LEFT
                    ##done = False

                elif event.key == pygame.K_RIGHT:
                    direction = RIGHT
                    ##done = False

        if direction == UP:
            newCell = {'x': coords[0]['x'], 'y': coords[0]['y']-1}

        elif direction == DOWN:
            newCell = {'x': coords[0]['x'], 'y': coords[0]['y']+1}

        elif direction == LEFT:
            newCell = {'x': coords[0]['x']-1, 'y': coords[0]['y']}

        elif direction == RIGHT:
            newCell = {'x': coords[0]['x']+1, 'y': coords[0]['y']}

        del coords[-1]

        coords.insert(0, newCell)
        setDisplay.fill(bg)
        drawCell(coords)
        pygame.display.update()
        fpsTime.tick(fps)

def drawCell(coords):
    for coord in coords:
        x = coord['x'] * cellSize
        y = coord['y'] * cellSize
        makeCell = pygame.Rect(x, y, cellSize, cellSize)
        pygame.draw.rect(setDisplay, white, makeCell)

while True:
    global fpsTime
    global setDisplay

    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption('controlling')
    gameMovement()
