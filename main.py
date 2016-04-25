import pygame
from random import randint
from OurSprite import OurSprite
from SpriteTileMap import SpriteTileMap
from SprayBottle import SprayBottle
from Food import Food
from Mold import Mold
pygame.init()

def main():
    #create display
    screen = pygame.display.set_mode((690, 601))
    screen.fill([156, 203, 250])

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 25)

    frameCount = 0
    frameRate = 10
    startTime = 90
    
    #tile map through which players will navigate
    fridgeMap = SpriteTileMap("maze.txt", "sprites.txt")

    #fPlayer navigates through the maze
    #sPlayer kills the mold, defends fPlayer
    fPlayer = Food()
    sPlayer = SprayBottle()

    #mold objects try to attack the food player
    mold1 = Mold('blue')
    mold2 = Mold('green')
    mold3 = Mold('blue')
    mold4 = Mold('green')
    mold5 = Mold('blue')
    mold6 = Mold('green')
    mold7 = Mold('blue')
    mold8 = Mold('green') 

    done = False
    
    #game loop 
    while not done:
        mouseX, mouseY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True                

            #arrow keys are assigned to the navigation movements
            #of fPlayer
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                fPlayer.move("RIGHT", fridgeMap)
                
            elif key[pygame.K_LEFT]:
                fPlayer.move("LEFT", fridgeMap)

            elif key[pygame.K_UP]:
                fPlayer.move("UP", fridgeMap)

            elif key[pygame.K_DOWN]:
                fPlayer.move("DOWN", fridgeMap)
            
            #sPlayer moves with the mouse
            if event.type == pygame.MOUSEMOTION:
                sPlayer.move(mouseX, mouseY)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mold1.decideNextState(sPlayer)
                mold2.decideNextState(sPlayer)
                mold3.decideNextState(sPlayer)
                mold4.decideNextState(sPlayer)
                mold5.decideNextState(sPlayer)
                mold6.decideNextState(sPlayer)

                print (isCollide(sPlayer,mold1))

        totalSeconds = startTime - (frameCount // frameRate)
        if totalSeconds < 0:
            totalSeconds = 0
        minutes = totalSeconds // 60
        seconds = totalSeconds % 60
        outputString = "Time left: {0:02}:{1:02}".format(minutes,seconds)

        text = font.render(outputString, True, (255,255,255))

        mold1.move()
        #mold2.move()
        #mold3.move()
        #mold4.move()
        #mold5.move()
        #mold6.move()

        frameCount += 1
        clock.tick(frameRate)
        
        pygame.display.flip()
        fridgeMap.drawMap(screen)
        screen.blit(fPlayer.getImage(), (fPlayer.getX(), fPlayer.getY()))
        screen.blit(mold1.getImage(), (mold1.getX(), mold1.getY()))
        screen.blit(mold2.getImage(), (mold2.getX(), mold2.getY()))
        screen.blit(mold3.getImage(), (mold3.getX(), mold3.getY()))
        screen.blit(mold4.getImage(), (mold4.getX(), mold4.getY()))
        screen.blit(mold5.getImage(), (mold5.getX(), mold5.getY()))
        screen.blit(mold6.getImage(), (mold6.getX(), mold6.getY()))
        screen.blit(sPlayer.getImage(), (sPlayer.getX(), sPlayer.getY()))
        pygame.draw.rect(screen, [250, 74, 47], [510, 10, 160, 40]) 
        screen.blit(text, [520, 23])

        #clock.tick()

    
main()
