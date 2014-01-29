import pygame

class Thing:
    def __init__(self, width, height, mass, speedlimit=.5, gravity = True):
        self.width = width
        self.height = height
        self.mass = mass
        self.surface = pygame.Surface((width,height))
        self.rect = self.surface.get_rect()
        self.surface.fill((255,255,255))
        self.speedlimit = speedlimit
        self.gravity = gravity
    
    def __repr__(self):
        return str(self.rect)
        

