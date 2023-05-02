import pygame.font

class Scoreboard():
    #represents gamescore info
    def __init__(self, ai_settings, screen, stats):#always self, game settings,screen to display on, stats has player score
        ##initialize typical stuff
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        #font color etc
        self.text_color = (255,0,0)
        self.font = pygame.font.SysFont(None, 48)
        #self.prep_score()
        #self.prep_lives()
        
    def prep_score(self):
        #renders score as an image
        score_str = f"{self.stats.score:,}"
        score_msg = "score: " + score_str
        self.stats_img = self.font.render(score_msg, True, self.text_color, self.ai_settings.bg_color)
        #display the score
        self.score_rect = self.stats_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        #draw to screen
        self.screen.blit(self.stats_img, self.score_rect)
        
    def prep_lives(self):
        #renders lives left as an image
        life_str = "lives: " + str(self.stats.ships_left)
        self.life_img = self.font.render(life_str, True, self.text_color, self.ai_settings.bg_color)
        self.life_rect = self.life_img.get_rect()
        self.life_rect.left = 20
        self.life_rect.top = 20
        
    def show_lives(self):
        self.screen.blit(self.life_img, self.life_rect)
        
#can probably learn more about classes and make a subclass for these.
#there's two types of scoreboards: lives, and points