import pygame as pg
class Settings():
    #a class for the game settings
    
    def __init__(self):
        #initialize settings
        ##Screen:
        self.screen_width = 1280    
        self.screen_height = 720
        self.bg_color = (0,0,0)
        self.bg = pg.image.load('literate-pancake/Alien_Invasion/image/stars.png')
        self.bg = pg.transform.scale(self.bg, (self.screen_width, self.screen_height))
        

        #we can modify these things here 
        
        #Ship properties
        self.ship_speed_factor = 2.5
        self.ship_limit = 5
        
        #bullet properties
        self.bullet_speed_factor = 1.5
        self.bullet_height = 15
        self.bullet_width = 5
        self.bullet_color= (255,0,0)
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet direction: negative left, positive right
        self.fleet_direction = 1 #could do left right but...
        #we'll multiple by this to flip direction