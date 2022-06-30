
from attr import has
import pygame
import game_mechanics
import buttons

pygame.init()

width = 1200
height = 900

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
green = (0,100,0)

game_font = pygame.font.SysFont("verdana",20)

space_between_question_piles = 150
padding_above_question_piles = 50


clock = pygame.time.Clock()
FPS = 30

WIN = pygame.display.set_mode((width,height))
pygame.display.set_caption("Friends against Humanity!")

def main():
    run = True
    player_size = 0
    user_input_text = ""
    keyboard_active = False
    player_name_entered = False
    index = 0
    question_press_status = False
    answer_press_status = False
    question_index = 0
    answer_index = 0
    has_winner = False
    winner = None
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and keyboard_active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_input_text = user_input_text[:-1]
                elif event.key == pygame.K_SPACE:
                    user_input_text += " "
                elif pygame.K_a<=event.key<=pygame.K_z:
                    user_input_text += event.unicode
        WIN.fill(white)
        if player_size == 0:
            player_size = initial_screen(player_size)
        elif player_name_entered == False:
            keyboard_active = True
            user_input_text, index, user_input_text, player_name_entered = take_player_name(user_input_text,index, user_input_text, player_name_entered)
            name_text = game_font.render(user_input_text,True,black)
            WIN.blit(name_text,(500,300))
        elif not has_winner:
            keyboard_active = False
            index, question_press_status, answer_press_status, question_index, answer_index = game_screen(index, question_press_status, answer_press_status, question_index, answer_index)
            if answer_press_status and question_press_status:
                card = game_mechanics.playerlist[index].current_pile_status()[answer_index]
                game_mechanics.playerlist[index].place_card(card)
                game_mechanics.question_list[question_index].add_to_pile(card.get_value(), card)
                if not game_mechanics.question_list[question_index].get_status():
                    buttons.question_button_list[question_index].inactive()
                    winning_player = game_mechanics.question_list[question_index].who_won_pile(game_mechanics.playerlist[index], game_mechanics.playerlist)
                    winning_player.win_pile()
                game_mechanics.draw_card(game_mechanics.playerlist[index])
                if game_mechanics.playerlist[index].current_piles_won()>(5//len(game_mechanics.playerlist)):
                    has_winner = True
                    winner = game_mechanics.playerlist[index]
                index += 1
                answer_press_status = False
                question_press_status = False
                for button in buttons.question_button_list:
                    if button.get_status():
                        button.refresh_button(buttons.question_button_img)
                for button in buttons.answer_button_list:
                    button.refresh_button(buttons.answer_button_img)
        else:
            winning_message = str(f'The winner is: {winner.get_name()}! Congratulations!')
            win_font = pygame.font.SysFont("verdana", 40,True)
            win_message_rendered = win_font.render(winning_message,True,black)
            WIN.blit(win_message_rendered,(int(width/2 - win_message_rendered.get_width()/2), int(height/2 - win_message_rendered.get_height()/2)))
        pygame.display.update()
    pygame.quit()


def initial_screen(player_size):
    WIN.fill((250,5,100))
    game_font = pygame.font.SysFont("arial",80,True)
    start_text = game_font.render("How many players will be playing?", True, (5,255,10))
    WIN.blit(start_text,(int((width - start_text.get_width())/2),int(height/4)))
    if buttons.two_player_button.draw(WIN):
        player_size = 2
    elif buttons.three_player_button.draw(WIN):
        player_size = 3
    elif buttons.four_player_button.draw(WIN):
        player_size = 4
    if player_size > 0:
        game_mechanics.initialise_game(player_size)
    return player_size


def take_player_name(player_name, index, reset_name, done):
    name_query = game_font.render("Please input player name: ", True, black)
    WIN.blit(name_query, (200,300))
    if buttons.continue_button.draw(WIN):
        game_mechanics.set_name_of_player(index,player_name)
        if index < len(game_mechanics.playerlist)-1:
            index += 1
            reset_name = ""
        else:
            reset_name = ""
            index = 0
            game_mechanics.deal_cards()
            done = True
    return player_name, index, reset_name, done


def game_screen(player_index, question_press_status,answer_press_status, question_index, answer_index):
    for i in range(5):
        header = f'Pile: {i+1}, Current pile value: {game_mechanics.question_list[i].get_value()}'
        header_text = game_font.render(header, True, red)
        question = "Question: " + str(game_mechanics.question_list[i].get_question())
        question_text = game_font.render(question,True,black)
        WIN.blit(header_text,(80,80+i*70))
        WIN.blit(question_text, (80, 100+i*70))

        #select a pile to answer
        if buttons.question_button_list[i].draw(WIN):
            question_press_status, question_chosen = buttons.question_button_list[i].press_status(question_press_status, buttons.question_button_img, buttons.question_button_pressed_img)
            if question_chosen:
                question_index = i


    player_index = player_index%len(game_mechanics.playerlist)
    current_player = game_mechanics.playerlist[player_index]
    current_player_text = str(f"Current player: {current_player.get_name()}, Number of piles owned: {current_player.current_piles_won()}")
    player_header_text = game_font.render(current_player_text,True,green)
    WIN.blit(player_header_text,(80,int(height/2)))


    for card in current_player.current_pile_status():
        card_index = current_player.current_pile_status().index(card)
        card_text = game_font.render(str(f'Card: {card_index+1}, {card.get_tag()}, Card value: {card.get_value()}'),True,blue)
        WIN.blit(card_text,(80,500+40*card_index))
        if buttons.answer_button_list[card_index].draw(WIN):
            answer_press_status, answer_chosen = buttons.answer_button_list[card_index].press_status(answer_press_status, buttons.answer_button_img, buttons.answer_button_pressed_img)
            if answer_chosen:
                answer_index = card_index

    return player_index, question_press_status, answer_press_status, question_index, answer_index



if __name__ == "main":
    main() #if this module is imported it will only do these line under this if block
    

main()

