import pygame
from pygame.locals import *
from environment import Environment
from thing import Thing
from constants import *
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
        
        self.speedlimit = {}
        self.speedlimit[UP] = 20
        self.speedlimit[DOWN] = 20
        self.speedlimit[LEFT] = 10
        self.speedlimit[RIGHT] = 10
        
        self.speed_decay = {}
        self.speed_decay[UP] = .1
        self.speed_decay[DOWN] = .01
        self.speed_decay[LEFT] = 1
        self.speed_decay[RIGHT] = 1
        
        #jumping vars
        self.gravity = True    
        self.jump_power = 30
        self.jump_power2 = 30
        self.jump_pause = False        
        self.walljump_power_right = False
        self.walljump_power_left = False
        self.walljumped = False
        
        
        #multiplayer vars
        self.multiplayer = True

    
    def __repr__(self):
        return self.name
    
    def jump(self, player, environment, keys_pressed):
        player_control = environment.get_controller(player)
        
        
        if player.jump_power > 0:
            for force in environment.forces[player]:
                    if force.direction == DOWN:
                        force.magnitude = 0
            player_control(Force(player.jump_power , UP))
            player.jump_power -= 1
            player.jump_pause = True
         
                       
        elif player.jump_power <= 0:           
            
            if player.jump_power2 > 0 and player.jump_pause == False:
                for force in environment.forces[player]:
                    if force.direction == DOWN:
                        force.magnitude = 0
                player_control(Force(player.jump_power2 , UP))
                
                if keys_pressed[K_a] and player.walljump_power_right > 0 and player.walljump_power_left == 0:
                    player_control(Force(player.jump_power2, RIGHT))
                    for force in environment.forces[player]:
                        if force.direction == LEFT:
                            force.magnitude = 0
                    player.walljump_power_right -= 1
                    
                if keys_pressed[K_d] and player.walljump_power_left > 0 and player.walljump_power_right == 0:
                    player_control(Force(player.jump_power2, LEFT))
                    for force in environment.forces[player]:
                        if force.direction == RIGHT:
                            force.magnitude = 0
                    player.walljump_power_left -= 1
                        
                player.jump_power2 -= 1
                
        else:
            player.jump_power = 0
            if player.jump_power2 < 15:
                player.jump_power2 = 0
            player.jump_pause = False
            player.walljump_power_right = 0
            player.walljump_power_left = 0
        
                