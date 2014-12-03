import pygame
from pygame.locals import *

import gamelib
from Grid import *


class Lightout(gamelib.SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	GREEN = pygame.Color('green')
   	
   	def __init__(self):
		super(Lightout, self).__init__('Light out', Lightout.WHITE)
		self.level = 1
		self.chk_Win = False 
		self.is_Start = True
		self.image = Image()
		self.IsClear_Stage = False
		self.Is_Called_HowToPlay = False

	def init(self):
		super(Lightout, self).init()
		self.light = Light(level = self.level)
		self.light.map_level(level = self.level)
		self.mouse_position = [0,0]
		self.is_First = self.is_clicked
		self.Repeat = 0
		self.count = 0

	def update(self):
		if pygame.mouse.get_pressed() == (1,0,0) and self.Is_Called_HowToPlay == False: # detect left click and check call HowToPlay
			self.On_clicked()
			pygame.time.wait(2000)
			self.Is_Called_HowToPlay = True 
		elif pygame.mouse.get_pressed() == (1,0,0) : # detect left click
			self.On_clicked()
			self.is_Start = False
		else:
			self.Repeat = 0
			self.Check_pass_Level()		
	
	def On_clicked(self):
		self.Repeat+=1
		if self.Repeat == 1 :
			if self.is_Start == False and self.IsClear_Stage == False:
				self.mouse_position = [self.posX,self.posY]
				self.light.light_on_click(self.level,self.mouse_position)
				#print self.mouse_position
			elif self.is_Start == False and self.IsClear_Stage == True:
				self.IsClear_Stage = False

	def Check_pass_Level(self):
		if  self.chk_Win == False:
			self.chk_Win = self.light.Check_win()
			if self.chk_Win == True:
				self.IsClear_Stage = True
				self.Call_NextLevel()

	def Call_NextLevel(self) :
		if self.level <3:
			self.chk_Win = False
			pygame.time.wait(2000)
			self.level += 1; 
			self.init()
		else :
			self.level = 4
			pygame.time.wait(2000)
			self.terminate()

	def render(self,surface):
		if self.is_Start:
			self.image.render(surface,self.Is_Called_HowToPlay)
		elif self.is_Start == False and self.IsClear_Stage == False:
			self.light.draw(surface,self.level)
		elif self.is_Start == False and self.IsClear_Stage == True:
			self.image.render_clear_stage(surface,self.level)

def main():
	game = Lightout()
	game.run()

if __name__ == '__main__':
	main()