import sys
import pygame as pg

def check_events(ship):
    #respond to keypresses
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()#exit unless other keys
        
        elif event.type == pg.KEYDOWN:#if a key's down
            if event.key == pg.K_RIGHT:
                ship.moving_right = True
            elif event.key == pg.K_LEFT:
                ship.moving_left = True
        
        elif event.type == pg.KEYUP:            
            if event.key == pg.K_RIGHT:
                ship.moving_right = False
            elif event.key == pg.K_LEFT:
                ship.moving_left = False
                
def update_screen(ai_settings, screen, ship):
    #redraw and update screen, go to new screen       
    screen.fill(ai_settings.bg_color)#set the background  while running from settings class
    ship.blitme()
    pg.display.flip() #draw new screen