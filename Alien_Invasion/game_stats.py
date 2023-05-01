class Game_stats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False #start game inactive

    def reset_stats(self):
        #initialize stats
        self.ships_left = self.ai_settings.ship_limit