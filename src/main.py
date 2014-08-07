import pygame, sys, json
from pygame.locals import *
from settings import *
from environment import Environment
from player import Player
from force import Force
from gravity import Gravity
from camera import Camera
from levels import Levels
from newmultiplayer import Client
from constants import *


def start_game():

    start_game_loop()
    
def check_for_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_w]:
        player_control(Force(5 , UP))
    if keys_pressed[K_s]:
        player_control(Force(5 , DOWN))
    if keys_pressed[K_a]:
        player_control(Force(5 , LEFT))
    if keys_pressed[K_d]:
        player_control(Force(5 , RIGHT))
    
    if keys_pressed[K_RETURN]:
        environment.positions[player_list[playername]] = [0, -100]
        camera.focus(player_list[playername].rect.center)    
    
    if keys_pressed[K_SPACE]:

        player_list[playername].jump(player_list[playername], environment, keys_pressed)
        
    if keys_pressed[K_SPACE] == False:
        player_list[playername]
        player_list[playername].jump_pause = False
        player_list[playername].jump_power = 0
        player_list[playername].walljump_power_right = 0
        player_list[playername].walljump_power_left = 0   
    
    if keys_pressed[K_v]:
        if player_list[playername].multiplayer:
            #client.purgepositions()
            pass                  

def update_screen():
    screen.fill((255,255,255))
    
    for thing in environment.things:
        screen.blit(thing.surface, camera.get_coords((thing.rect.x, thing.rect.y)))
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
        camera.mouse_focus(player_list[playername].rect.center, pygame.mouse.get_pos())
        
        
        if player_list[playername].multiplayer:
            client.upload_position((player_list[playername].name,player_list[playername].rect.x, player_list[playername].rect.y, player_list[playername].rect.width, player_list[playername].rect.height))
            
            player_positions = client.download_positions()
            for player_names in player_positions:
                if player_names not in player_list:
                    print 'player_position:', player_names, 'player_postions: ', player_positions, 'player_positions[player_position],', player_positions[player_names]
                    player_list[player_names] = Player(player_names, player_positions[player_names][2], player_positions[player_names][3])
                    environment.add(player_list[player_names], (player_list[player_names].rect.x, player_list[player_names].rect.y))

            for player_names in player_list:
                print 'player_list[playernames]', player_list[player_names]
                print 'player_posiots', player_positions[player_names]
                player_list[player_names].rect.x, player_list[player_names].rect.y, player_list[player_names].rect.width, player_list[player_names].rect.height = player_positions[player_names]     
                
        update_screen()
        clock.tick(60)               


if __name__ == '__main__':

    pygame.init()

    playername = 'pp?'
    player_size_x, player_size_y = 20,40 
    
    screen = pygame.display.set_mode((xreso,yreso))
    clock = pygame.time.Clock()
    camera = Camera(0,0)
    
    player_list = {} 
    player_list[playername] = Player(playername, player_size_x, player_size_y)
    environment = Environment()
    level = Levels()
    level.load_level1(environment, player_list[playername])    
    player_control = environment.get_controller(player_list[playername])
    
    player_list[playername].multiplayer = True
    if player_list[playername].multiplayer:
        client = Client(('68.36.84.150' , 7777))


    start_game_loop()
    
