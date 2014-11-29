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
		self.light = Light(level = self.level)
		self.light.map_level(level = self.level)
		self.mouse_position = [0,0]
		self.is_First = self.is_clicked
		self.Repeat = 0


	def init(self):
		super(Lightout, self).init()
		#self.render_score()
	def mouse(self):
		pass

	def update(self):
		if pygame.mouse.get_pressed() == (1,0,0): # detect left click
			self.Repeat+=1
			if self.Repeat == 1:
				self.mouse_position = [self.posX,self.posY]
				self.light.light_on_click(self.level,self.mouse_position)
				print self.mouse_position
		else:
			self.Repeat = 0
	
	#def render_score(self):
	#	self.score_image = self.font.render("Score = %d" % self.score, 0, Lightout.WHITE)

	def render(self,surface):
		self.light.draw(surface,self.level)
		#self.player.render(surface)
		#surface.blit(self.score_image, (10,10))
def main():
	game = Lightout()
	game.run()

if __name__ == '__main__':
	main()