#OurSprite.py
#
# Author: Caroline Requierme
# Date: March 28, 2016
# Class: CITA 280
# Assignment: Assignment 4
#
# Purpose: create a class OurSprite that represents a game
#          sprite in terms of its character symbol (such as
#          'K' for knight), its filename, and its Pygame
#          Sprite object used for blit drawing
#

class OurSprite:

    # receive arguments for character symbol, a string filename (such as
    # "knight.png") , and pygame sprite object. Assume that the given
    # pygame sprite has been created and loaded by Pygame
    
    def __init__(self,symbol,filename,pysprite):
        self.symbol = symbol
        self.filename = filename
        self.pygameSprite = pysprite

    # What is the symbol of our sprite?
    def getSymbol(self):
        return self.symbol

    # What is the filename of our sprite?
    def getFileName(self):
        return self.filename

    # What is the Pygame sprite object of our sprite?
    def getPygameSprite(self):
        return self.pygameSprite
        
