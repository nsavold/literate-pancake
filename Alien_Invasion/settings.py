class Settings():
    #a class for the game settings
    
    def __init__(self):
        #initialize settings
        ##Screen:
        self.screen_width = 1440
        self.screen_height = 1000
        self.bg_color = (235,235,235)
        #we can modify these things here 
        
        #Ship properties
        self.ship_speed_factor = 2.5
        
        #bullet properties
        self.bullet_speed_factor = 1
        self.bullet_height = 15
        self.bullet_width = 5
        self.bullet_color= (255,0,0)
        self.bullets_allowed = 3