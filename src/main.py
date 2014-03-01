import pygame
from pygame.locals import *
from environment import Environment
from player import Player
from force import Force
from gravity import Gravity
from math import pi
from tiles import Tiles


def start_game():

    start_game_loop()
    
def check_for_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
                
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_w]:
        player_control(Force(6 , -pi/2))
    if keys_pressed[K_s]:
        player_control(Force(6 , pi/2))
    if keys_pressed[K_a]:
        #if player.walljump_power <= 0 or player.jump_power2 == 0:
        player_control(Force(6 , pi))
    if keys_pressed[K_d]:
        player_control(Force(6 , 0))
    
    if keys_pressed[K_RETURN]:
        environment.positions[player] = [600, 400]
    
    if keys_pressed[K_SPACE]:
        
        if player.jump_power > 0:
            player_control(Force(player.jump_power , -pi/2))
            player.jump_power -= 1
            player.gravity = False
         
                       
        elif player.jump_power <= 0:          
            player.gravity = True  
            
            if player.jump_power2 > 0 and player.doublejump_delay <= 0:
                for force in environment.forces[player]:
                    if force.direction == pi/2:
                        force.magnitude = 0
                player_control(Force(player.jump_power2 , -pi/2))
                
                if keys_pressed[K_a] and player.walljump_power_right > 0 and player.walljump_power_left == 0:
                    player_control(Force(player.jump_power2, 0))
                    for force in environment.forces[player]:
                        if force.direction == pi:
                            force.magnitude = 0
                    player.walljump_power_right -= 1
                    
                if keys_pressed[K_d] and player.walljump_power_left > 0 and player.walljump_power_right == 0:
                    player_control(Force(player.jump_power2, pi))
                    for force in environment.forces[player]:
                        if force.direction == 0:
                            force.magnitude = 0
                    player.walljump_power_left -= 1
                        
                player.jump_power2 -= 1
                player.gravity = False
                
        print player.gravity, player.jump_power2
        if player.jump_power == False and player.jump_power2 == False:
            player.gravity = True
    else:
        player.jump_power = 0
        if player.jump_power2 < 15:
            player.jump_power2 = 0
        player.gravity = True
        player.doublejump_delay -= 1
        player.walljump_power_right = 0
        player.walljump_power_left = 0

                                    
    

def update_screen():
    screen.fill((0,0,0))
    
    for thing in environment.things:
        #screen.blit(thing.surface, get_screen_position(environment.positions[thing]))
        screen.blit(thing.surface, environment.positions[thing])
    pygame.display.update()
    
def start_game_loop():#GAME LOOP________________________________________________________________

    while 1:

        check_for_events()
        environment.advance()
        update_screen()
        clock.tick(60)

        

if __name__ == '__main__':
    pygame.init()
    x_reso = 1280
    y_reso = 720
    screen = pygame.display.set_mode((x_reso,y_reso))
    clock = pygame.time.Clock()
    
    player = Player(20,30,1)
    long_tile = Tiles(300,30,2)
    tall_tile = Tiles(30,400,2)
    tall_tile2 = Tiles(30,400,2)
    square_tile = Tiles(200,200,2)
    
    environment = Environment()
    environment.add(player, (0,100))   
    environment.add(long_tile, (900,400))
    environment.add(tall_tile, (400, 100))
    environment.add(tall_tile2, (100, 100))
    environment.add(square_tile, (600,500)) 
    
    
    player_control = environment.get_controller(player)

    start_game_loop()
    
#whut happened to deh git test
