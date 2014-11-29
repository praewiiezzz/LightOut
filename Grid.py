import pygame
from pygame.locals import *
from random import randint

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
            self.stage = self.random_stage(level)
            self.grid = self.create_map(size[level],stage[level],width[level],height[level],margin)


    def random_stage(self,level):
        if level == 2:
            stage1 = [[0,1,0,0,0],[1,1,1,0,0],[0,1,0,1,0],[0,1,1,1,1],[0,0,0,1,0]]
            stage2 = [[1,1,1,0,0],[1,1,1,1,1],[0,1,1,1,1],[0,0,1,0,1],[0,0,0,0,1]]      
            stage3 = [[1,1,1,1,1],[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,1],[0,1,0,0,0]]  
            stage4 = [[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,1,0,1,1],[1,0,0,1,1]]  
            stage5 = [[0,0,1,0,1],[0,1,0,1,1],[0,1,1,0,0],[0,1,1,1,1],[1,1,1,1,1]]  
            stage = [stage1,stage2,stage3,stage4,stage5]
        return stage[randint(1,5)]
        if level == 3:
            pass

    def create_map(self,size,stage,width,height,margin):
        grid = []
        stage = self.stage   
        size = 5
        for row in range(size):
            grid.append([])
            for column in range(size):
                grid[row].append(0) # Append a cell
                grid[row][column] = stage[row][column]
                print ("row",row,"column",column)
        return grid
        
    def light_on_click(self,level,pos):
        grid = self.grid
        size = 5
        #for row in range(size):
        #    grid.append([])
        #    for column in range(size):
        #        grid[row].append(0) # Append a cell
        width = 88
        height = 88
        margin = 10 # This sets the margin between each cell
        self.pos = pos
        column = self.pos[0] //(width + margin)
        row = self.pos[1] //(height + margin)
        print("Click ", self.pos, "Grid coordinates: ",row,column)
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
        grid = self.grid
        #for row in range(size):
        #    grid.append([])
        #    for column in range(size):
        #        grid[row].append(0) # Append a cell

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