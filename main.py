import pygame
from pygame.locals import *

import gamelib
from Grid import *

class Lightout(gamelib.SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	GREEN = pygame.Color('green')
   	
   	def __init__(self):
		super(Lightout, self).__init__('Light out', Lightout.BLACK)
		self.light = Light(level = 2)
		self.light.map_level()
		self.mouse_position = [0,0]
		self.is_First = self.is_clicked
		self.Repeat = 0


	def init(self):
		super(Lightout, self).init()
		#self.render_score()
	def mouse(self):
		pass

	def update(self):
		#event = pygame.event.get() # User did something	

		if pygame.mouse.get_pressed() == (1,0,0):
			self.Repeat+=1
			if self.Repeat == 1:
				self.mouse_position = [self.posX,self.posY]
				print self.mouse_position
		else:
			self.Repeat = 0
	
	#def render_score(self):
	#	self.score_image = self.font.render("Score = %d" % self.score, 0, Lightout.WHITE)

	def render(self,surface):
		self.light.draw(surface)
		#self.player.render(surface)
		#surface.blit(self.score_image, (10,10))
def main():
	game = Lightout()
	game.run()

if __name__ == '__main__':
	main()