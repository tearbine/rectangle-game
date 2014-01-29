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
        player_control(Force(6 , pi))
    if keys_pressed[K_d]:
        player_control(Force(6 , 0))
    
    if keys_pressed[K_SPACE] and player.jump_power > 0:
        print 'hi'
        for force in environment.forces[player]:
            if force.direction == pi/2:
                del force
        player_control(Force(player.jump_power , -pi/2))
        player.jump_power -= 1
        player.gravity = False
    else:
        player.jump_power = 0
        player.gravity = True                    

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
    tile = Tiles(300,30,2)
    tile2 = Tiles(30,400,2)
    
    environment = Environment()
    environment.add(player, (0,100))   
    environment.add(tile, (800,400))
    environment.add(tile2, (200, 100)) 
    
    
    player_control = environment.get_controller(player)

    start_game_loop()
    
#git test take 2
