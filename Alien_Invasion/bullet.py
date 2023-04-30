from typing import Any
import pygame as pg
from pygame.sprite import Sprite #sprites a class lol
#it lets us group bullets!

class Bullet(Sprite):#inherit form the sprite class
    def __init__(self, ai_settings, screen, ship):
        #create a bullet at the tip of the ship(where a bullet starts from)
        super().__init__()
        self.screen = screen
        
        #create a bullet then move it to the right spot, with size specified by settings.py
        self.rect = pg.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)#top left
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top #put the bullet at the ship tip
        
        #make it a float for smooth movement
        self.y = float(self.rect.y) #rect.x, rect.y for location
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    #update bullet
    def update(self):
        ##move it
        #update decimal position
        self.y -= self.speed_factor
        #update rect
        self.rect.y = self.y
        #(x doesnt change)

    #draw bullet
    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect)