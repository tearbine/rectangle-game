import pygame
from environment import Environment
from thing import Thing
from math import pi
from force import Force
import random

class Player(Thing):
    def __init__(self, name, width, height, mass=1, speedlimit=.5):
        Thing.__init__(self, width, height, mass, speedlimit=.5)
        
        self.name = name
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.font = pygame.font.SysFont('monospace',30)
        self.name_graphic = self.font.render(self.name, 1, (0,0,0))
        self.name_graphic_rect = pygame.Surface.get_rect(self.name_graphic)
        
        self.surface.fill(self.color)
        
        
        #jumping vars
        self.gravity = True    
        self.jump_power = 15
        self.jump_power2 = 15
        self.doublejump_delay = 0        
        self.walljump_power_right = False
        self.walljump_power_left = False
        
        
        #multiplayer vars
        self.multiplayer = True

    
    def __repr__(self):
        return self.name
        
                