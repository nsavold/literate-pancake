import sys
import pygame as pg
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()#exit unless other keys
        elif event.type == pg.KEYDOWN:#keys in other method
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:            
            check_keyup_events(event, ship)

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

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
                        
def get_num_of_aliens_x(ai_settings, alien_width): #how many fit on the screen (wide)
    available_space_x = ai_settings.screen_width - 2*alien_width #our screen width, minus a gap of 2 aliens
    num_aliens_x = int(available_space_x/(2*alien_width)) #how many spaces for alien + space between
    return num_aliens_x

def get_num_of_rows(ai_settings, ship_height, alien_height):
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

def update_screen(ai_settings, screen, ship, aliens, bullets):
    #redraw and update screen, go to new screen       
    #sscreen.fill(ai_settings.bg_color)
    #draw_bg(ai_settings, screen) #this one is all funcky...
    screen.blit(ai_settings.bg.convert(), (0, 0))      #this does it just once      
    ship.blitme()
    aliens.draw(screen)
    #redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pg.display.flip() #draw new screen
    
def update_bullets(bullets):
    for bullet in bullets.copy():#copy the group then loop over it so you dont remove
        if bullet.rect.bottom <= -5:
            bullets.remove(bullet) 