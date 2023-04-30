class Settings():
    #a class for the game settings
    
    def __init__(self):
        #initialize settings
        ##Screen:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (235,235,235)
        #we can modify these things here 
        
        #Ship properties
        self.ship_speed_factor = 5.5