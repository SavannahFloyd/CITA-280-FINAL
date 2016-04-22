#OurSpriteInventory.py
#
# Author: Caroline Requierme
# Date: March 28, 2016
# Class: CITA 280
# Assignment: Assignment 4
#
# Purpose: create a class OurSpriteInventory that provides a list
#          inventory of OurSprite objects allowing us to retrieve an
#          OurSprite by its symbol

from OurSprite import OurSprite

class OurSpriteInventory:

    # create an empty list to hold OurSprite objects
    def __init__(self):
        self.sprites = []

    # add a received OurSprite object (assume that it has
    # been fully initialized) to the inventory, return True
    # when the sprite is added
    def addSprite(self, sp):
        self.sprites.append(sp)
        return True

    # receive a character symbol and return OurSprite
    # object whose symbol matches given symbol, return None
    # if no objects match
    def getBySymbol(self, givenSymbol):
        i = 0
        result = None
        while result == None and i < len(self.sprites):
            current = self.sprites[i].getSymbol()
            if current == givenSymbol:
                result = self.sprites[i]
            else:
                return result
