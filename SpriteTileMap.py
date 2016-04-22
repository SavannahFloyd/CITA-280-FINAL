#SpriteTileMap.py
#
# Author: Caroline Requierme
# Date: March 28, 2016
# Class: CITA 280
# Assignment: Assignment 4
#
# Purpose: Represent the 2D grid of symbols that define a tile map's contents
#          and an OurSpriteInventory that holds the sprite tiles used in
#          drawing the map
# Input: Text file with map data-- a rectangular grid of text
#        symbols which will represent images on a map
#        Example:
#        . . . .
#        * . . ^
#        $ . . ^
#
#        Text file with sprite data -- list of attributes needed
#        to create a pygame sprite object (symbol, filename)
#        example: ". grass_128.png"
#
import pygame
from OurSprite import OurSprite
from OurSpriteInventory import OurSpriteInventory

class SpriteTileMap:

    pygame.init()
    
    # Create text map and OurSprite objects from data files
    def __init__(self, mapData, spriteData):
        # Create an empty list to represent text map
        # tileMap will be a list of lists
        # Each row will consist of a list of symbols
        self.tileMap = []

        # Open map data file
        mapInfile = open(mapData, "r")

        # Loop through lines of input file
        for line in mapInfile:
            # Split line into individual symbols
            # Assume a space between symbols 
            mapLineSplit = line.split()
            
            # mapLineSplit now contains a list of character symbols
            # mapLineSplit is appended as a row to mapRows
            self.tileMap.append( mapLineSplit )

        # Close map data file
        mapInfile.close()

        # Set number of rows and columns
        self.numRows = len(self.tileMap)
        self.numCols = len(self.tileMap[0])

        # Create inventory of sprites
        self.sprites = OurSpriteInventory()

        # Open sprite data file
        spriteInfile = open(spriteData, "r")

        # Loop through lines of input file
        for line in spriteInfile:
            # Split line into a list of sprite attributes
            # spriteLineSplit will contain symbbol at index 0, and filename
            # at index 1 ex: ['.', "grass_126.png"]
            spriteLineSplit = line.split()

            self.sprites = OurSpriteInventory()
            self.spriteSize = 32

            # Load sprite into pygame to create pygame sprite object
            pySprite = pygame.image.load(spriteLineSplit[1])
            
            # Create OurSprite object from line information
            sp = OurSprite(spriteLineSplit[0],spriteLineSplit[1], pySprite)

            # Add new sprite to inventory
            self.sprites.addSprite(sp)

    # Print symbols of map row by row
    def printMap(self):

        # Loop through rows in map
        for r in range(self.numRows):
            # Create an empty string to represent row
            rowText = ""
            # Loop through symbols in curret row
            for c in range(self.numCols):
                # Concatenate each symbol
                rowText += str(self.tileMap[r][c])
            # Print current row
            print(rowText)

    def drawMap(self, screen):
        # Initialize coordinates to one sprite length less than 0
        # This way, the first sprite will be drawn with its top left corner
        # at (0, 0) on the grid
        x = 0 - self.spriteSize
        y = 0 - self.spriteSize
        # Loop through the rows in the map
        # Increment after the whole row has been drawn
        for row in range(self.numRows):
            y = y + self.spriteSize
            # Loop through the columns in the row
            # Increment after each symbol is drawn
            for col in range(self.numCols):
                x = x + self.spriteSize
                # Decide which sprite to use by its symbol
                currentSymbol = self.tileMap[row][col]
                currentSprite = self.sprites.getBySymbol(currentSymbol)
                screen.blit(currentSprite, (x,y))
                
    # accessors
    def getSpriteSize(self):
        return self.spriteSize
    def getNumRows(self):
        return self.numRows
    def getNumCols(self):
        return self.numCols
