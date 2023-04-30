import pygame as pg
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #start game and create a screen for it
    pg.init()
    ai_settings = Settings()#ai for alien invasion
    screen = pg.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion")
    
    #make ship
    ship = Ship(ai_settings,screen)
    #set options:
    
    #start the "main" loop:
    while True:#while running
        gf.check_events(ship)
        ship.update()#after check event
        gf.update_screen(ai_settings, screen, ship) 
        
        
run_game()