import pygame as pg

class Ship():
    
    def __init__(self, ai_settings, screen):
        #init
        self.screen = screen
        self.ai_settings = ai_settings
        #movement flags
        self.moving_right = False
        self.moving_left = False
        WHITE = (255,255,255)
        
        #load ship, get a rectangle size, make bg transparent
        #change which line is uncommented to change enemy ship
     
        self.image = pg.image.load('Alien_Invasion/image/ship.bmp') 
        self.image = pg.transform.scale(self.image, ai_settings.player_ship_size)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() # our screen has a rectangle for collision
        
        #start the ship at the bottom center
        #centerx is the  coord of the center, centery is is y
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx    
            
    def update(self):
        #position updates basd on movement flags
        if self.moving_left and self.rect.left > 0: #rectleft not at edge
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        #update rect
        self.rect.centerx = self.center
    
    def blitme(self):
        #draw it at runtime in a_i.py
        self.screen.blit(self.image, self.rect)
        #when the screen updates, draw image at rectangle