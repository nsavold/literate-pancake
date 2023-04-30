import pygame as pg
from pygame.sprite import Group, Sprite

class Alien(Sprite):
    ##represents one enemy

    def __init__(self, ai_settings, screen):
        #init alien and where it starts
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        SHIP_SIZE = (50, 40)
        WHITE = (255,255,255)

        #load image, change size, make it transparent
        self.image = pg.image.load('literate-pancake/Alien_Invasion/image/enemyship.png')#for great justice find a ship
        self.image = pg.transform.scale(self.image, SHIP_SIZE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        #start it at zero
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #but zero is SLIGHTLY more than zero so the whole ship appears

        #make position a float
        self.x = float(self.rect.x)

    def blitme(self):
        #draw it
        self.screen.blit(self.image, self.rect)