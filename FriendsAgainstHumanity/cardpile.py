from operator import index
from random import randint


class QuestionPile:
    def __init__(self,image) -> None:
        self.cardlist = []
        self.pilevalue = 0
        self.active = True
        self.img = image

    def set_question(self,question_list):
        index = randint(0,len(question_list)-1)
        self.question = question_list.pop(index)
    
    def get_question(self):
        return self.question

    def get_value(self):
        return self.pilevalue
    
    def add_to_pile(self,card_value, card):
        self.cardlist.append(card)
        if self.pilevalue + card_value == 13:
            self.pilevalue = "Inactive"
            self.active = False
            self.just_nice = True
        elif self.pilevalue + card_value > 13:
            self.pilevalue = "Inactive"
            self.active = False
            self.just_nice = False
        else:
            self.pilevalue += card_value

    def get_status(self):
        return self.active

    def who_won_pile(self, current_player, player_list):
        if self.just_nice == True:
            return current_player
        elif self.just_nice == False:
            index = randint(0,len(player_list)-1)
            return player_list[index]

class AnswerCards:
    def __init__(self,value,answer,image) -> None:
        self.value = value
        self.tag = answer
        self.img = image
    
    def get_value(self):
        return self.value

    def get_tag(self):
        return self.tag


question_cards = ["Your friend is going through a tough time and tells you about something very personal.",
                  "One of your close friends confessed they have a crush on you but you do not feel the same.",
                  "What do you think of the person on your right?",
                  "What is the most memorable thing you do together with your friend/ partner?",
                  "Together we can achieve _____.",
                  "What is something you have always wanted to tell the left person but couldn't?",
                  "Back in my time, I had to ______.",
                  "I fell in love with them because ______.",
                  "When you hit your lowest, who do you seek help from?",
                  "What’s one thing you always wanted to do, but hesitate to do it",
                  "What’s something that makes you feel loved?",
                  "What is something you personally do not like in a potential partner? Be honest!",
                  "If the person next to you complimented you right now, what would be your reply?",
                  "Which sounds like something the person after you would say?"
                 ]


answers = ["Give them a hug",
            "Tell them you will do it next time",
            "World domination",
            "Kinky and hot",
            "It's Goofy time!!!",
            "I do too!",
            "I feel the same as you!",
            "When you find out .... you are broke..n",
            "Me, myself and I.",
            "You have daddy/mummy issues",
            "Overly clingy partners",
            "We are hotties",
            "Beautiful.",
            "Kind, respectful, gracious, accomplished and sweet",
            "A good pair of listening ears.",
            "LifeLine NUS - 6516 7777",
            "Jobs.",
            "School",
            "You are one smort gurl/boi",
            "Getting Covid-19",
            "Beauty is on the inside.",
            "Traveling 10,000 miles to see you",
            "Calling out your name",
            "Peace out",
            "Being cheapskate",
            "Dancing in the rain",
            "Spending big on someone",
            "Controlling freak",
            "Harassment and disrespect",
            "Turn me down when I need help",
            "Dancing at the top of the world",
            "Fitting in an uncomfortable environment to feel like somebody",
            "Hold me and take me anywhere",
            "Bad lies",
            "Feelings",
            "My best friend",
            "Family",
            "Nah fam",
            "Holding your hand",
            "Fat mood",
            "Just vibing",
            "Take with a pinch of salt",
            "Where are you now when I need you.",
            "Holiday mood",
            "Thank you for believing in me",
            "Tell my mama I love her"
            ]

answer_pile = []
for answer in answers:
    value = randint(1,4)
    answer_pile.append(AnswerCards(value,answer,image=None))

class AnswerPile:
    def __init__(self) -> None:
        self.pile = [i for i in answer_pile]

    def draw_card(self):
        index = randint(0, len(self.pile)-1)
        return self.pile.pop(index)
    
    def cards_left(self):
        return len(self.pile)