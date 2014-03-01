import pygame
from environment import Environment
from thing import Thing
from math import pi
from force import Force

class Player(Thing):
    def __init__(self, width, height, mass, speedlimit=.5):
        Thing.__init__(self, width, height, mass, speedlimit=.5)
        self.gravity = True
    
        self.jump_power = 15
        self.jump_power2 = 15
        self.doublejump_delay = 0
        
        self.walljump_power_right = False
        self.walljump_power_left = False
    '''def jump(self, thing, environment):
        print 'yolo1'
        print str(environment.things)
        forces = environment.forces[thing]
        for force in forces:
            print 'yolo2'
            if force.direction == -pi/2:
                print 'yolo'
                environment.forces[self].remove(force)
        environment.forces[thing].append(Force(10, pi/2))'''
    
    def __repr__(self):
        return 'Player'
        
                