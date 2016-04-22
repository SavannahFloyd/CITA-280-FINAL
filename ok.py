import pygame
pygame.init()
screen = pygame.display.set_mode((700, 700))
done = False

sprayBottle = pygame.image.load('SB120.png')
#sprayBottleX = 100
#sprayBottleY = 100
#screen.blit(sprayBottle, (sprayBottleX, sprayBottleY))

while not done:
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            

    pygame.display.flip()
    screen.blit(sprayBottle, mouseX, mouseY)
