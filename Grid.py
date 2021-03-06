import pygame
from pygame.locals import *
from random import randint

class Light(object):
    WHITE = pygame.Color('white')
    # color 1
    HOTPINK = (255, 102, 102)
    PINK = (255, 204, 204)
    # color 2
    HOTBLUE = ( 0, 204, 204)
    BLUE = ( 153, 255, 255)
    # color 3 
    HOTGREEN = ( 153, 255, 0)
    GREEN = ( 221, 255, 155)
    # color 4
    HOTPEACH = ( 255, 178, 102)
    PEACH = ( 255, 229, 204)
    # color 5
    HOTGRAY = ( 160, 160, 160)
    GRAY = ( 224, 224, 224)
    # color 6
    HOTYELLOW = ( 255, 255, 0)
    YELLOW = ( 255, 255, 153)

    def __init__(self, level):
        self.level = level
        self.IsWin = False

    def map_level(self,level):
        self.size = [0,3,5,7]
        self.width = [0,153,88,60]
        self.height = [0,153,88,60]
        self.margin = 10 # This sets the margin between each cell
        self.stage = self.random_stage(level)
        self.Color_Lightout = self.Color()
        self.grid = self.create_map(self.size[level],self.stage[level],self.width[level],self.height[level],self.margin)
    
    def stage_level1(self,level):
        stage1 = [[1,0,1],[0,1,1],[1,0,1]]
        stage2 = [[0,1,0],[1,1,1],[1,1,1]]
        stage3 = [[0,1,0],[0,1,1],[1,1,1]]
        stage4 = [[1,1,0],[0,0,1],[0,0,0]]
        stage5 = [[1,1,1],[0,1,0],[1,1,0]]
        stage = [stage1,stage2,stage3,stage4,stage5]
        return stage

    def stage_level2(self,level):
        stage1 = [[0,1,0,0,0],[1,1,1,0,0],[0,1,0,1,0],[0,1,1,1,1],[0,0,0,1,0]]
        stage2 = [[1,1,1,0,0],[1,1,1,1,1],[0,1,1,1,1],[0,0,1,0,1],[0,0,0,0,1]]      
        stage3 = [[1,1,1,1,1],[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,1],[0,1,0,0,0]]  
        stage4 = [[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,1,0,1,1],[1,0,0,1,1]]  
        stage5 = [[0,0,1,0,1],[0,1,0,1,1],[0,1,1,0,0],[0,1,1,1,1],[1,1,1,1,1]]  
        stage = [stage1,stage2,stage3,stage4,stage5]
        return stage

    def stage_level3(self,level):
        stage1 = [[1,1,1,0,0,1,0],[1,0,1,0,0,0,1],[1,0,0,1,0,1,0],[0,1,0,1,0,0,1],[1,1,1,0,0,1,0],[0,1,0,1,1,1,1],[1,0,0,1,0,0,1]]
        stage2 = [[0,1,1,0,0,0,0],[0,0,0,0,1,0,1],[0,1,1,1,0,1,0],[0,1,0,1,0,1,1],[1,0,1,0,1,0,1],[1,1,1,1,0,0,0],[0,1,1,0,0,0,0]]     
        stage3 = [[0,0,1,0,1,0,1],[1,1,1,0,1,0,0],[1,0,1,1,0,0,1],[0,1,1,1,0,0,1],[1,0,0,0,0,1,1],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0]] 
        stage4 = [[0,0,0,1,1,1,1],[1,0,1,0,0,0,0],[0,0,1,1,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0]] 
        stage5 = [[0,0,1,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,1,0],[1,0,1,1,0,0,1],[1,0,0,1,1,1,1],[0,0,1,1,0,1,0],[1,1,1,0,0,1,0]] 
        stage = [stage1,stage2,stage3,stage4,stage5]
        return stage

    def random_stage(self,level):
        if level == 1:
            stage = self.stage_level1(level)
        elif level == 2:
            stage = self.stage_level2(level)
        elif level == 3:
            stage = self.stage_level3(level)
        self.call_stage = stage[randint(0,4)]
        return self.call_stage

    def create_map(self,size,stage,width,height,margin):
        grid = []
        stage = self.stage   
        for row in range(size):
            grid.append([])
            for column in range(size):
                grid[row].append(0) # Append a cell
                grid[row][column] = stage[row][column]
        return grid
        
    def light_on_click(self,level,pos):
        grid = self.grid
        self.pos = pos
        column = self.pos[0] //(self.width[level] + self.margin)
        row = self.pos[1] //(self.height[level] + self.margin)
        self.Light_On_Off(row,column,grid,level)        

    def Light_On_Off(self,row,column,grid,level):
        grid[row][column] = int(not grid[row][column])
        if 0 <= (row+1)<self.size[level]  :
            grid[row+1][column] = int(not grid[row+1][column])
        if 0 <= (row-1)<self.size[level]  :
            grid[row-1][column] = int(not grid[row-1][column])
        if 0 <= (column+1)<self.size[level]  :
            grid[row][column+1] = int(not grid[row][column+1])
        if 0 <= (column-1)<self.size[level]  :
            grid[row][column-1] = int(not grid[row][column-1]) 

    def Color(self): 
        Color_Lightout = [] 
        if self.level == 1:
            Color_Lightout = [[Light.YELLOW,Light.HOTYELLOW],[Light.GREEN,Light.HOTGREEN]]
        elif self.level == 2:
            Color_Lightout = [[Light.PINK,Light.HOTPINK],[Light.BLUE,Light.HOTBLUE]]
        elif self.level == 3:
            Color_Lightout = [[Light.PEACH,Light.HOTPEACH],[Light.GRAY,Light.HOTGRAY]]
        return Color_Lightout[randint(0,1)]          

    def Check_win(self):
        if self.IsWin == True:
            return True
        else :
            return False
    
    def draw(self,surface,level):
        count = 0
        grid = self.grid
        for row in range(self.size[level]):
            for column in range(self.size[level]):
                color = self.Color_Lightout[0]
                if grid[row][column] == 1:
                    color = self.Color_Lightout[1]
                self.draw_block(surface,level,row,column,color)
                count += grid[row][column]
                
        if (count == 0) :
            self.IsWin = True

    def draw_block(self,surface,level,row,column,color):
        pygame.draw.rect(surface,
                        color,
                        [(self.margin+self.width[level])*column+self.margin,
                        (self.margin+self.height[level])*row+self.margin,
                        self.width[level],
                        self.height[level]])


class Image(object):

    def __init__(self):
        self.img_clear_stage = [0,"res/1.jpg","res/2.jpg","res/3.jpg"]

    def render(self,surface,Is_called):
        if Is_called == False:
            self.pic = pygame.image.load("res/intro.jpg")
        else :
            self.pic = pygame.image.load("res/howtoplay.jpg")
        surface.blit(self.pic,(0,0))

    def render_clear_stage(self,surface,level):
        self.pic = pygame.image.load(self.img_clear_stage[level-1])
        surface.blit(self.pic,(0,0))
        