from game import Game2v2

class GameEnv:
    def __init__(self) -> None:
        self.termination = False
        self.player_list = [0, 1, 2, 3]
        self.current_player_id = 0
        self.last_play_id = -1
        self.game = Game2v2()
        self.winner = -1

    def reset(self):
        self.termination = False
        self.player_list = [0, 1, 2, 3]
        self.current_player_id = 0
        self.last_play_id = -1
        self.game = Game2v2()

    def next(self):
        self.current_player_id = self.current_player_id + 1 if self.current_player_id < 3 else 0
        if self.current_player_id == self.last_play_id:
            self.game.new_turn()

    def last(self, show_info = True):
        player_id = self.current_player_id
        can_play = self.game.check_play(self.current_player_id)
        observation = self.game.see_cards(self.current_player_id)
        termination = self.termination
        if show_info and not termination:
            print("----------------------")
            print("player", self.current_player_id, ":")
            print("    cards holding:", observation)
            print("    can play a card:", can_play)
        return player_id, can_play, observation, termination

    def step(self, action, show_info = True):
        if self.game.check_play(self.current_player_id) and action:
            card = self.game.play_card(self.current_player_id)
            self.last_play_id = self.current_player_id
            if show_info:
                print("player", self.current_player_id, "->", card)
            if self.game.check_win() > -1:
                self.termination = True
                self.winner = self.current_player_id
        else:
            if show_info:
                print("player", self.current_player_id, "pass")

        self.next()

    def report(self, show_info = True):
        result = {}
        result["winner"] = (0, 2) if self.winner%2==0 else (1, 3)
        if show_info:
            print("----------------------")
            print("winner:", result["winner"])
        return result

        

