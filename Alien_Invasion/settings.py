import pygame as pg
class Settings():
    #a class for the game settings
    
    def __init__(self):
        #initialize settings
        ##Screen:
        self.screen_width = 1280    
        self.screen_height = 720
        self.bg_color = (0,0,0)
        self.bg = pg.image.load('Alien_Invasion/image/stars.png')
        self.bg = pg.transform.scale(self.bg, (self.screen_width, self.screen_height))
        #we can modify these things here 
        
        #Ship properties
        self.ship_limit = 3
        
        #bullet properties
        self.bullet_height = 25
        self.bullet_width = 10
        self.bullet_color= (255,0,0)
        self.bullets_allowed = 4

        #alien settings
        self.fleet_drop_speed = 10
        #fleet direction: negative left, positive right
        
        
        #speedup settings
        self.speedup_scale = 1.1
        #initialize changing settings
        self.initialize_dynamic_settings()
        
    #changing settings      
    def initialize_dynamic_settings(self): # most of these settings we moved into the dynamic category
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2.5
        self.alien_speed_factor = 1.1
        self.alien_drop_pause = 5 #unused right now. how can we have the aliens stop for a biit when they hit the edge
        self.fleet_direction = 1 #could do left right but...we'll multiple by this to flip direction
    
    def increase_speed(self): #multiply what we increase by the speedup scale
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_drop_pause /= self.speedup_scale
    #we call this when we kill the whole fleet