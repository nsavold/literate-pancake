import pygame as pg
from pygame.sprite import Group, Sprite

class Alien(Sprite):
    ##represents one enemy

    def __init__(self, ai_settings, screen):
        #init alien and where it starts
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        WHITE = (255,255,255)

        #load image, change size, make it transparent
        #comment out all but one line of the enemy ships for dinnfer ones
        self.image = pg.image.load('Alien_Invasion/image/enemyship.bmp')#generic
        self.image = pg.transform.scale(self.image, ai_settings.alien_ship_size)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        #start it at zero
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #but zero is SLIGHTLY more than zero so the whole ship appears

        #make position a float
        self.x = float(self.rect.x)
    
    def check_edges(self):
        ##if edge then return true
        screen_rect = self.screen.get_rect()
        if self.rect.right  >= screen_rect.right: #right side
            return True
        elif self.rect.left <= 0: #if alien's at left edge, 
            return True

    
    def update(self):
        ##move right or left depending on fleet direction
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x#move the alien to the right

    def blitme(self):
        #draw it
        self.screen.blit(self.image, self.rect)