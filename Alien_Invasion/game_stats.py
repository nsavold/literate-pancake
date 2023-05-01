class Game_stats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False #start game inactive

    def reset_stats(self): # we do this when we hit play! what else should happen when we hit play?
        #initialize stats
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0