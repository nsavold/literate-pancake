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
    #make stats object, and scoreboard/lives counter
    stats = Game_stats(ai_settings)             #passed to most functions
    sb = Scoreboard(ai_settings, screen, stats)
    sb.prep_score()
    lc = Scoreboard(ai_settings, screen, stats)
    lc.prep_lives()
    #make play button
    p_button = Button(ai_settings, screen, "Click to Play")
    #TODO: refactor for a new Group() of HUD elements?
    
    
    #start the "main" loop:
    while True:#while running
        gf.check_events(ai_settings, screen, stats, lc, sb, p_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()#after check event
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, lc, ship, aliens, bullets) 
        gf.update_screen(ai_settings, screen, stats, sb, lc, ship, aliens, bullets, p_button)
        
        
        
        
run_game()
