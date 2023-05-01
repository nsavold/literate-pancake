import sys
import pygame as pg
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, stats, p_button, ship, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()#exit unless other keys
        elif event.type == pg.MOUSEBUTTONDOWN:
            m_x, m_y = pg.mouse.get_pos()
            check_play_button(stats, p_button, m_x, m_y)
        elif event.type == pg.KEYDOWN:#keys in other method
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:            
            check_keyup_events(event, ship)

def check_play_button(stats, p_button, m_x, m_y):
    #new game when play clicked
    if p_button.rect.collidepoint(m_x, m_y):
            stats.game_active = True

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        ship.moving_right = True
    elif keys[pg.K_LEFT]:
        ship.moving_left = True
    elif keys[pg.K_SPACE]: #create boolet
        fire_bullet(ai_settings, screen, ship, bullets)
    elif keys[pg.K_LSHIFT] and keys[pg.K_q]:
        sys.exit()     

def check_keyup_events(event, ship): #no bullet here
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_LEFT:
        ship.moving_left = False

def fire_bullet(ai_settings, screen, ship, bullets):#fires bullet if allowed
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
                        
def get_num_of_aliens_x(ai_settings, alien_width): #how many aliens in a row
    available_space_x = ai_settings.screen_width - 2*alien_width #our screen width, minus a gap of 2 aliens
    num_aliens_x = int(available_space_x/(2*alien_width)) #how many spaces for alien + space between
    return num_aliens_x

def get_num_of_rows(ai_settings, ship_height, alien_height):# how many alien rows we allow to spawn
    ##rows that can fit with buffer between player/fleet
    availaible_space_y = (ai_settings.screen_height- (7*alien_height)-ship_height)#gap = 7 rows + player
    number_rows = int(availaible_space_y/(2*alien_height))#rows = space available/alien+empty space
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number): #make and place in row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width #our aliens are as wide as their rect
    alien.x = alien_width + 2*alien_width*alien_number #it starts at the next open space based on
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number                              # how many are placed
    aliens.add(alien) #add to group

def create_fleet(ai_settings, screen, ship, aliens): #uses the  functions above to decide aliens to create
    #create all our aliens #its based on screen width!!!
    alien = Alien(ai_settings, screen)
    num_aliens_x = get_num_of_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_num_of_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range (num_aliens_x):#first row
            create_alien(ai_settings, screen, aliens, alien_number, row_number) #make alien

'''def draw_bg(ai_settings, screen):#we tried, but realized it was esier to just make a big backgorund with stars and scale it
    i, j = 0,0
    bg_space_x, bg_space_y = (int(ai_settings.screen_width/ai_settings.bg.get_width()) +2), (int(ai_settings.screen_height/ai_settings.bg.get_height()) +2)
    for x_space in range(bg_space_x):
        for y_space in range(bg_space_y):
            screen.blit(ai_settings.bg.convert(), (i, j))#set the background  while running from settings class
            i += ai_settings.bg.get_width() 
        i = 0
        j += ai_settings.bg.get_height()'''

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, p_button):#call sprite updates
    #redraw and update screen, go to new screen       
    screen.blit(ai_settings.bg.convert(), (0, 0))      #this does it just once      
    ship.blitme()
    aliens.draw(screen)
    #redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #if the game is inactive draw button
    if not stats.game_active:
        p_button.draw_button()
    pg.display.flip() #draw new screen

def update_bullets(ai_settings, screen, ship, bullets, aliens):#update our bullets themseves
    #check if the bullets hit the top
    for bullet in bullets.copy():#copy the group then loop over it so you dont remove
        if bullet.rect.bottom <= -5:
            bullets.remove(bullet)
    bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):#what happens if the ship is hit
    ##respond to hits
    if stats.ships_left > 0:
        stats.ships_left -= 1    #you die
        aliens.empty()
        bullets.empty()         #get rid of stuff
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()      #make new stuff
        sleep(0.8) #pause for player recognition
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):#are the aliens at the bottom of screen?
    #if an alien hits the bottom, lose a life
    screen_rect = screen.get_rect()#get screen size from the screen that was passed
    for alien in aliens.sprites():#for every alien in the fleet
        if alien.rect.bottom >= screen_rect.bottom: #if the alien is passed the bottom of the screen
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets) #run the routine when the ship is hit
            break #check once come back

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):#update all aliens in fleet
    check_fleet_edges(ai_settings, aliens)
    aliens.update()#aliens the gorup
    #if aliens hit the ship, game over
    if pg.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    #if aliens hit the bottom, game over
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def change_fleet_direction(ai_settings, aliens):#flip the direction pointer for which way ships go
    #drop fleet, switch direciton of all aliens
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed #drop them all
    ai_settings.fleet_direction *= -1 #flip the direction of the ships

def check_fleet_edges(ai_settings, aliens):#check if the aliens are at the left/right edge then flip
    #if the alien hits the edge, respond
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break #check em once, then stop, we come back  

def bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):#pew pew pow
    collisions = pg.sprite.groupcollide(bullets, aliens, True, True) 
    if len(aliens) == 0:#if we empty fleet
        bullets.empty() #remove all bullets
        create_fleet(ai_settings, screen, ship, aliens)

