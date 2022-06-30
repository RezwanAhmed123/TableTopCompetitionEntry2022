class Player:
    def __init__(self) -> None:
        self.card_pile = []
        self.number_of_piles_won = 0
    
    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def draw_card(self,card):
        self.card_pile.append(card)

    def place_card(self,card):
        self.card_pile.remove(card)

    def current_pile_status(self):
        return self.card_pile

    def show_pile(self):
        for card in self.card_pile:
            print(f'Card Value: {card.get_value()}, Card Tag: {card.get_tag()}')
        
    def win_pile(self):
        self.number_of_piles_won += 1

    def current_piles_won(self):
        return self.number_of_piles_won

