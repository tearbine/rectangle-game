import pygame
from environment import Environment
from thing import Thing
from math import pi
from force import Force

class Player(Thing):
    gravity = True
    
    jump_power = 15
    jump_power2 = 15
    doublejump_delay = 0
    
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
        
                