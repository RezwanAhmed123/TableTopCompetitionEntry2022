from random import randint
import players
import cardpile


current_answer_pile = cardpile.AnswerPile()
hand_size = 6
playerlist = []
question_list = []

def initialise_game(number_of_players):
    for player in range(number_of_players):
        player = players.Player()
        playerlist.append(player)

def set_name_of_player(index, name):
    playerlist[index].set_name(name)

def deal_cards():
    for player in playerlist:
        for i in range(hand_size):
            player.draw_card(current_answer_pile.draw_card())

def draw_card(player):
    if current_answer_pile.cards_left()>0:
        player.draw_card(current_answer_pile.draw_card())

game_question_pile = [i for i in cardpile.question_cards]

def get_questions():
    for i in range(5):
        questionpile = cardpile.QuestionPile("Nil")
        questionpile.set_question(game_question_pile)
        question_list.append(questionpile)
    return question_list

question_list = get_questions()