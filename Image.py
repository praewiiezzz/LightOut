import pygame
from pygame.locals import *
from random import randint

class Image(object):
	def __init__(self):
		self.intro_pic = "res/intro.jpg"

	def render(self,surface):
		self.image = self.pygame.image.load(self.intro_pic)
		surface.blit(self.image,(0,0))

	def render_clear_stage(self,surface):
		self.image = self.pygame.image.load(self.intro_pic)
		surface.blit(self.image,(0,0))