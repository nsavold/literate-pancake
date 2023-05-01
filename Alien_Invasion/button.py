'''play button and i suppose a class to make others with'''
import pygame.font
class Button():

    def __init__(self, ai_settings, screen, msg): #msg: pass button a messgae
        #get screen stuff
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #button properties #gee i wonder how we'll refactor this
        self.width, self.height = 250, 50
        self.button_color = (50, 200, 50)#Green!
        self.text_color = (0,0,0) #black
        self.font = pygame.font.SysFont(None, 48)

        #build button and cente ron the screen
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #prep butotn message
        self.prep_msg(msg)

    def prep_msg(self, msg):
        ##turn the message into the image and slap on the button
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)#has backgorund color of the button its on
        self.msg_img_rect = self.msg_img.get_rect() # img rect 
        self.msg_img_rect.center = self.rect.center #center the button image on the button

    def draw_button(self):
        #draw button and message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)