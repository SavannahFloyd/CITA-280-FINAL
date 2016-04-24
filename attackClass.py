from foodClass import Food
from moldClass import Mold
#from sprayBottle import sprayBottle
from random import randint 

def attack(mold, food):
    ## if mold sprite overlays food sprite
    ## damage should be done to the food

    ## if moldSprite touches the foodSprite:
    ##      implement hurt on food HP
    maxHurt = food.getHitPoints() - mold.getBasicDamage()
    hurt = randint(maxHurt // 2, maxHurt)
    hp = food.getHitPoints()
    hp = hp - hurt
    if hp < 0:
        hp = 0
    food.setHitPoints(hp)
    return hurt

def main():
    foodSprite = Food(100)
    moldSprite = Mold(5)
    ## spray bottle stuff maybe
    while foodSprite.getHitPoints() > 0:
        attack(moldSprite, foodSprite)
        ## if spraybottle clicks over mold:
        ##      mold is killed/ reset to the beginning 
    if foodSprite.getHitPoints() <= 0:
        print("YOU LOSE!")
        print("GAME OVER!")
    ## elif foodSprite makes it to the exit with hp > 0
    ##      YOU WIN! GAME OVER!
        
        
