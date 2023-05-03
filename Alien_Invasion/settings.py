import pygame as pg
class Settings():
    #a class for the game settings
    
    def __init__(self):
        #initialize settings
        ##Screen:
        self.screen_width = 1280    
        self.screen_height = 720
        self.bg_color = (0,0,0)
        self.bg = pg.image.load('Alien_Invasion/image/stars.gif')#literate-pancake needs to be the acitve directory in terminal
        self.bg = pg.transform.scale(self.bg, (self.screen_width, self.screen_height))
        #we can modify these things here 
        
        #Ship properties
        self.ship_limit = 3
        self.player_ship_size = (50,60)  #60, 72 is file's original size
        
        #bullet properties
        self.bullet_height = 25
        self.bullet_width = 10             #modify for testing. 10 normally
        self.bullet_color= (255,0,0)
        self.bullets_allowed = 4

        #alien settings
        self.fleet_drop_speed = 8            #####modify for testing. 8 normally
        self.alien_ship_size = (40, 32)
        
        
        #speedup settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        #initialize changing settings
        self.initialize_dynamic_settings()
        
    #changing settings      
    def initialize_dynamic_settings(self): # most of these settings we moved into the dynamic category
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2.5
        self.alien_speed_factor = .75         ###modify for testing. .75 normally
        self.alien_drop_pause = 5 #unused right now. how can we have the aliens stop for a biit when they hit the edge
        self.fleet_direction = 1 #could do left right but...we'll multiple by this to flip direction
       #points for aliens
        self.alien_points = 50
            
    def increase_speed(self): #multiply what we increase by the speedup scale
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_drop_pause /= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        
    #we call this when we kill the whole fleet