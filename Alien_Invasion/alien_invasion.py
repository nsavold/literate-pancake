import pygame as pg
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group #group is a class?
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #start game and create a screen for it
    pg.init()
    ai_settings = Settings()                    #passed to most functions
    screen = pg.display.set_mode(               #passed to most functions
        (ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion") #window name
    #make ship
    ship = Ship(ai_settings,screen)             #passed to most functions
    #make a group for bullets
    bullets = Group()                           #passed to most functions
    #make alien group and fleet
    aliens = Group()                            #passed to most functions
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #make stats and scoreboard
    stats = Game_stats(ai_settings)             #passed to most functions
    sb = Scoreboard(ai_settings, screen, stats)
    #make play button
    p_button = Button(ai_settings, screen, "Click to Play")
    
    
    #start the "main" loop:
    while True:#while running
        gf.check_events(ai_settings, screen, stats, p_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()#after check event
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets) 
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, p_button)
        #right now we freeze when run out of lives and stop updating the screen
        
        
        
run_game()
