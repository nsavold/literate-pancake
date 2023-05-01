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
        self.prep_score()
        
    def prep_score(self):
        #renders score as an image
        score_str = str(self.stats.score)
        self.stats_img = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        #display the score
        self.score_rect = self.stats_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        #draw to screen
        self.screen.blit(self.stats_img, self.score_rect)