import pygame
from pygame.locals import *

class Light(object):


    def __init__(self, level):
        self.level = level

    def map_level(self):
            level = 2
            self.level = level
            size = [0,3,5,7]
            stage = [0,1,2,3]
            width = [0,153,88,60]
            height = [0,153,88,60]
            margin = 10 # This sets the margin between each cell
            self.create_map(size[level],stage[level],width[level],height[level],margin)
            #draw(size[level],stage[level],width[level],height[level],margin)
            #self.light_on_click(size[level])

    def create_map(self,size,stage,width,height,margin):
        grid = []
        size = 5
        for row in range(size):
            grid.append([])
        for column in range(size):
            grid[row].append(0) # Append a cell
        """grid[1][3] = 1
        #grid[0][4] = 1
        #grid[2][2] = 1
        grid[2][3] = 1
        #grid[2][3] = 1
        grid[3][1] = 1
        grid[3][3] = 1
        grid[4][0] = 1
        grid[4][2] = 1
        """
    def light_on_click(self,level,pos):
            size = 5
            column = self.pos[0] // (width + margin)
            row = self.pos[1] // (height + margin)
            # Set that location to zero
            grid[row][column] = int(not grid[row][column])
            print grid[row][column]
            if 0 <= (row+1)<size :
                grid[row+1][column] = int(not grid[row+1][column])
                print grid[row+1][column]
            if 0 <= (row-1)<size :
                grid[row-1][column] = int(not grid[row-1][column])
                print grid[row-1][column]
            if 0 <= (column+1)<size :
                grid[row][column+1] = int(not grid[row][column+1])
                print grid[row][column+1]
            if 0 <= (column-1)<size :
                grid[row][column-1] = int(not grid[row][column-1])
                print grid[row][column-1]

    def draw(self,surface):
        size = 5
        width = 88
        height = 88
        margin = 10 # This sets the margin between each cell
        grid = []
        for row in range(size):
            grid.append([])
            for column in range(size):
                grid[row].append(0) # Append a cell
        WHITE = pygame.Color('white')
        GREEN = pygame.Color('green')

        for row in range(size):
            for column in range(size):
                color = GREEN
                if grid[row][column] == 1:
                    color = WHITE
                pygame.draw.rect(surface,
                                color,
                                [(margin+width)*column+margin,
                                (margin+height)*row+margin,
                                width,
                                height])
        pygame.display.flip()