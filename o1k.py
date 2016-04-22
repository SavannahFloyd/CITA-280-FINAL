import pygame
sprayBottle = pygame.image.load("C:\\Users\\Savannah\\Pictures\\sprites\\COIN.png")
screen = pygame.display.set_mode((700, 800))
done = False
sprayBottleX = 100
sprayBottleY = 100


while not done:
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    pygame.display.flip()
    screen.blit(sprayBottle, (mouseX, mouseY))
