import random

class Game2v2:
    def __init__(self) -> None:
        cards = list(range(1, 11)) + list(range(1, 11))
        random.shuffle(cards)
        self.player_cards = {
            0: cards[0:5],
            1: cards[5:10],
            2: cards[10:15],
            3: cards[15:20]
        }

        self.player_cards[0].sort()
        self.player_cards[1].sort()
        self.player_cards[2].sort()
        self.player_cards[3].sort()

        self.last_card = 0 # 0 - game start or new turn for same player

    def show_cards(self):
        print("player 0 cards", self.player_cards[0])
        print("player 1 cards", self.player_cards[1])
        print("player 2 cards", self.player_cards[2])
        print("player 3 cards", self.player_cards[3])

    # if a player can play a card
    def check_play(self, id):
        return self.player_cards[id][-1] > self.last_card

    def play_card(self, id):
        for i in range(5):
            if self.player_cards[id][i] > self.last_card:
                self.last_card = self.player_cards[id][i]
                self.player_cards[id][i] = 0
                self.player_cards[id].sort()
                return self.last_card
            
    def see_cards(self, id):
        return self.player_cards[id]

    # the player get a new turn when other player cannot play a card    
    def new_turn(self):
        self.last_card = 0

    # if any player win the game
    def check_win(self):
        for i in range(4):
            if self.player_cards[i][-1] == 0:
                # player i win
                return i
        # game continue
        return -1
