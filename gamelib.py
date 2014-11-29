import pygame
from pygame.locals import *

class SimpleGame(object):

    def __init__(self,
                 title,
                 background_color,
                 window_size=(500,500),
                 fps=60):
        self.title = title
        self.window_size = window_size
        self.fps = fps
        self.background_color = background_color
        self.posX = 0
        self.posY = 0
        self.is_terminated = False
        self.is_clicked = False

    def __game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)
        self.font = pygame.font.SysFont

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print "eiei"
                self.is_clicked = True
                print self.is_clicked
                self.on_click(self.is_clicked)


    def terminate(self):
        self.is_terminated = True

    def run(self):
        self.init()
        while not self.is_terminated:
            self.__handle_events()

            self.update()

            self.surface.fill(self.background_color)
            self.render(self.surface)
            pygame.display.update()

            self.clock.tick(self.fps)

    def init(self):
        self.__game_init()

    def update(self):
        pass

    def render(self,surface):
        pass

    def on_click(self,click):
        self.click = click
        if self.click == True:
            print "pos"
            self.get_pos()
            self.is_clicked = False
            self.click == self.is_clicked

    def get_pos(self):
        self.pos = pygame.mouse.get_pos()
        self.posX = self.pos[0]
        self.posY = self.pos[1]
        print ("pos",self.pos)