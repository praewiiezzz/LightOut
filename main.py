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
		self.light = Light(2)
		self.light.map_level()

	def init(self):
		super(Lightout, self).init()
		#self.render_score()

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
				pos = pygame.mouse.get_pos()
				self.light.light_on_click(level,pos)
	
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