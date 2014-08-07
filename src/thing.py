import pygame
from constants import *

class Thing:
    id = 0
    def __init__(self, width, height, mass, speedlimit=.5):
        self.width = width
        self.height = height
        self.mass = mass
        self.surface = pygame.Surface((width,height))
        self.rect = self.surface.get_rect()
        self.surface.fill((255,255,255))
        self.speed_decay = {UP: .01, DOWN : .01, LEFT : .01, RIGHT : .01}    
        self.speedlimit = {UP: speedlimit, DOWN : speedlimit, LEFT : speedlimit, RIGHT : speedlimit}      
        self.gravity = False
        self.colliding = False
        self.id = Thing.id
        Thing.id += 1
    
    def __repr__(self):
        return str('Thing')
        

