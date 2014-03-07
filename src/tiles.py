import pygame
from thing import Thing

class Tiles(Thing):
    def __init__(self, width, height, mass=2, surface=pygame.Surface((0,0)), speedlimit=2):
        Thing.__init__(self, width, height, mass, speedlimit=2)
        self.surface.fill((127,127,127))
        self.mass = 2
        self.gravity = False
    
    def __repr__(self):
        return str(self.rect)