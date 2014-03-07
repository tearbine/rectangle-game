import pygame, sys
from pygame.locals import *
from settings import *
from environment import Environment
from player import Player
from force import Force
from gravity import Gravity
from math import pi
from camera import Camera
from levels import Levels
from multiplayer import Client


def start_game():

    start_game_loop()
    
def check_for_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                
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
        environment.positions[player_list[playername]] = [0, 0]
        camera.focus(player_list[playername])
    
    if keys_pressed[K_SPACE]:
        
        if player_list[playername].jump_power > 0:
            player_control(Force(player_list[playername].jump_power , -pi/2))
            player_list[playername].jump_power -= 1
            player_list[playername].gravity = False
         
                       
        elif player_list[playername].jump_power <= 0:          
            player_list[playername].gravity = True  
            
            if player_list[playername].jump_power2 > 0 and player_list[playername].doublejump_delay <= 0:
                for force in environment.forces[player_list[playername]]:
                    if force.direction == pi/2:
                        force.magnitude = 0
                player_control(Force(player_list[playername].jump_power2 , -pi/2))
                
                if keys_pressed[K_a] and player_list[playername].walljump_power_right > 0 and player_list[playername].walljump_power_left == 0:
                    player_control(Force(player_list[playername].jump_power2, 0))
                    for force in environment.forces[player_list[playername]]:
                        if force.direction == pi:
                            force.magnitude = 0
                    player_list[playername].walljump_power_right -= 1
                    
                if keys_pressed[K_d] and player_list[playername].walljump_power_left > 0 and player_list[playername].walljump_power_right == 0:
                    player_control(Force(player_list[playername].jump_power2, pi))
                    for force in environment.forces[player_list[playername]]:
                        if force.direction == 0:
                            force.magnitude = 0
                    player_list[playername].walljump_power_left -= 1
                        
                player_list[playername].jump_power2 -= 1
                player_list[playername].gravity = False
                
        if player_list[playername].jump_power == False and player_list[playername].jump_power2 == False:
            player_list[playername].gravity = True
    else:
        player_list[playername].jump_power = 0
        if player_list[playername].jump_power2 < 15:
            player_list[playername].jump_power2 = 0
        player_list[playername].gravity = True
        player_list[playername].doublejump_delay -= 1
        player_list[playername].walljump_power_right = 0
        player_list[playername].walljump_power_left = 0   
    
    if keys_pressed[K_v]:
        client.purgepositions()
                              

def update_screen():
    screen.fill((255,255,255))
    
    for thing in environment.things:
        screen.blit(thing.surface, camera.get_coords(environment.positions[thing]))
        if hasattr(thing, 'name_graphic'):
            thing.name_graphic_rect.center = thing.rect.center
            thing.name_graphic_rect.y -= 40
            screen.blit(thing.name_graphic, camera.get_coords((thing.name_graphic_rect.x, thing.name_graphic_rect.y)))
    pygame.display.update()
    
def start_game_loop():#GAME LOOP________________________________________________________________

    while 1:

        check_for_events()
        environment.advance()
        camera.scroll(player_list[playername])
        
        
        if player_list[playername].multiplayer:
            client.sendpositions(playername, player_list[playername].rect.x, player_list[playername].rect.y, player_list[playername].rect.width, player_list[playername].rect.height)
            
            player_positions = client.recvpositions()
            for c_player in player_positions:
                try:
                    environment.positions[player_list[c_player]] = player_positions[c_player][0], player_positions[c_player][1]                    
                except KeyError:
                    player_list[c_player] = Player(c_player, player_positions[c_player][2], player_positions[c_player][3])
                    environment.add(player_list[c_player], (player_positions[c_player][0], player_positions[c_player][1]))

                
        update_screen()
        clock.tick(60)               


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((xreso,yreso))
    clock = pygame.time.Clock()
    camera = Camera(0,0)
    playername = raw_input('Enter name: ')
    player_size_x, player_size_y = int(raw_input('Enter width (must be pls reasonable number (like around 30)): ')) , int(raw_input('Enter height (must be reeznubl number): '))
    
    player_list = {}
    player_list[playername] = Player(playername, player_size_x, player_size_y)
    environment = Environment()
    level = Levels()
    level.load_level2(environment, player_list[playername])    
    player_control = environment.get_controller(player_list[playername])
    
    client = Client('68.36.84.150', 7777)
    player_list[playername].multiplayer = True

    start_game_loop()
    
#whut happened to deh git test
