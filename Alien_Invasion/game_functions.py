import sys
import pygame as pg
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()#exit unless other keys
        elif event.type == pg.KEYDOWN:#keys in other method
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:            
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pg.K_LEFT:
        ship.moving_left = True
    elif event.key == pg.K_SPACE: #create boolet
        fire_bullet(ai_settings, screen, ship, bullets)
        

def check_keyup_events(event, ship): #no bullet here
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_LEFT:
        ship.moving_left = False

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
                        
def update_screen(ai_settings, screen, ship, bullets):
    #redraw and update screen, go to new screen       
    screen.fill(ai_settings.bg_color)#set the background  while running from settings class
    ship.blitme()
    #redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pg.display.flip() #draw new screen
    
def update_bullets(bullets):
    for bullet in bullets.copy():#copy the group then loop over it so you dont remove
        if bullet.rect.bottom <= -5:
            bullets.remove(bullet) 