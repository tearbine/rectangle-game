import pygame
from settings import *
class Camera():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.scroll_left = 0
        self.scroll_right = 0
        self.scroll_up = 0
        self.scroll_down = 0
        
        self.rect = pygame.Rect(x,y,xreso,yreso)
    
    def get_coords(self, (x, y)):
        camera_x = x - self.rect.x
        camera_y = y - self.rect.y
        return camera_x, camera_y
    
    def focus(self, thing):
        self.rect.center = thing.rect.center
    def scroll(self, thing):
        if thing.rect.x < self.rect.x + (xreso/3):
            self.scroll_left = 10
        if thing.rect.x > self.rect.right - (xreso/3):
            self.scroll_right = 10   
        if thing.rect.y < self.rect.y + (yreso/3):
            self.scroll_up = 10
        if thing.rect.y > self.rect.bottom - (yreso/3):
            self.scroll_down = 10  
                  
        if self.scroll_left:
            self.rect.x -= self.scroll_left
            if thing.rect.x > self.rect.x + xreso/3:
                self.scroll_left = 0    
        if self.scroll_right:
            self.rect.x += self.scroll_right
            if thing.rect.x < self.rect.right - xreso/3:
                self.scroll_right = 0             
        if self.scroll_up:
            self.rect.y -= self.scroll_up
            if thing.rect.y > self.rect.y + yreso/3:
                self.scroll_up = 0   
        if self.scroll_down:
            self.rect.y += self.scroll_down
            if thing.rect.y < self.rect.bottom - yreso/3:
                self.scroll_down = 0