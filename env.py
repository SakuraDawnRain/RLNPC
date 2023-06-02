from game import Game2v2

class GameEnv:
    def __init__(self) -> None:
        self.termination = False
        self.player_list = [0, 1, 2, 3]
        self.current_player_id = 0
        self.last_play_id = -1
        self.game = Game2v2()

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

    def last(self):
        player_id = self.current_player_id
        can_play = self.game.check_play(self.current_player_id)
        observation = self.game.see_cards(self.current_player_id)
        termination = self.termination
        return player_id, can_play, observation, termination

    def step(self, action):
        if self.game.check_play(self.current_player_id) and action:
            card = self.game.play_card(self.current_player_id)
            self.last_play_id = self.current_player_id
            print("player", self.current_player_id, "-> ", card)
            if self.game.check_win() > -1:
                self.termination = True
        self.next()
