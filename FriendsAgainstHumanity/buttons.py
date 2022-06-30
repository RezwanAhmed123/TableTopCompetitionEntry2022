import pygame
import cardpile

pygame.init()

width = 1200
height = 900

class Buttons:
    def __init__(self,x,y,img,scale) -> None:
        self.width = img.get_width()
        self.height = img.get_height()
        self.scale = scale
        self.img = pygame.transform.scale(img, (int(self.width*scale),int(self.height*scale)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.status = False
        self.active = True

    def draw(self, surface):
        action = False

        mouse_position = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.img, (self.rect.x, self.rect.y))

        return action
    
    def press_status(self,another_button_already_pressed, current_img, alt_img):
        if self.active:
            if self.status == False and not another_button_already_pressed:
                self.img = pygame.transform.scale(alt_img, (int(self.width*self.scale),int(self.height*self.scale)))
                self.status = True
                another_button_already_pressed = True
                chosen = True
            elif self.status == True:
                self.img = pygame.transform.scale(current_img, (int(self.width*self.scale),int(self.height*self.scale)))
                self.status = False
                another_button_already_pressed = False
                chosen = False
            else:
                chosen = False
        else:
            chosen = False
        return another_button_already_pressed, chosen

    def refresh_button(self,original_image):
        self.img = pygame.transform.scale(original_image, (int(self.width*self.scale),int(self.height*self.scale)))
        self.status = False

    def inactive(self):
        self.active = False
        self.img = pygame.transform.scale(inactive_button_img, (int(self.width*self.scale),int(self.height*self.scale)))

    def get_status(self):
        return self.active


        
        



#choose number of players buttons
player_button_x = width/8
player_button_y = height*3/5
player_button_scale = 0.8

two_player_button_img = pygame.image.load("two_player_button.png")
two_player_button = Buttons(player_button_x, player_button_y ,two_player_button_img,player_button_scale)

three_player_button_img = pygame.image.load("three_player_button.png")
three_player_button = Buttons(player_button_x + 300, player_button_y ,three_player_button_img,player_button_scale)

four_player_button_img = pygame.image.load("four_player_button.png")
four_player_button = Buttons(player_button_x + 650, player_button_y ,four_player_button_img,player_button_scale)


# continue button
continue_button_img = pygame.image.load("continue_button.png")
continue_button = Buttons(width*3/4, height*2/7, continue_button_img,player_button_scale)

# Question Buttons
question_button_list = []
question_button_img = pygame.image.load("question_button.png")
question_button_pressed_img = pygame.image.load("question_button_alt.png")
for i in range(5):
    question_button_list.append(Buttons(30,90+i*70, question_button_img, 0.4))

#Answer Buttons
answer_button_list = []
answer_button_img = pygame.image.load("answer_button_image.png")
answer_button_pressed_img = pygame.image.load("answer_button_alt_image.png")
for i in range(6):
    answer_button_list.append(Buttons(30,500+40*i, answer_button_img, 0.3))

#inactive button
inactive_button_img = pygame.image.load("inactive_image.png")