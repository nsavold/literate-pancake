import pygame as pg
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group #group is a class?

def run_game():
    #start game and create a screen for it
    pg.init()
    ai_settings = Settings()#ai for alien invasion
    screen = pg.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion")
    
    #make ship
    ship = Ship(ai_settings,screen)
    #make a group fro bullets
    bullets = Group()

    
    #start the "main" loop:
    while True:#while running
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()#after check event
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
       
        
        
        
run_game()