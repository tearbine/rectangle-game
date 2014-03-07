import pygame

class Thing:
    id = 0
    def __init__(self, width, height, mass, speedlimit=.5):
        self.width = width
        self.height = height
        self.mass = mass
        self.surface = pygame.Surface((width,height))
        self.rect = self.surface.get_rect()
        self.surface.fill((255,255,255))
        self.speedlimit = speedlimit
        self.gravity = False
        self.colliding = False
        self.id = Thing.id
        Thing.id += 1
    
    def __repr__(self):
        return str('Thing')
        

