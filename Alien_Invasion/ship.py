import pygame as pg

class Ship():
    
    def __init__(self, ai_settings, screen):
        #init
        self.screen = screen
        self.ai_settings = ai_settings
        #movement flags
        self.moving_right = False
        self.moving_left = False
        
        #load ship, get a rectangle size
        self.image = pg.image.load('literate-pancake/Alien_Invasion/image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start the ship at the bottom center
        #centerx is the  coord of the center, centery is is y
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
            
    def update(self):
        #position updates basd on movement flags
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        #update rect
        self.rect.centerx = self.center
    
    def blitme(self):
        #draw it at runtime in a_i.py
        self.screen.blit(self.image, self.rect)
        #when the screen updates, draw image at rectangle