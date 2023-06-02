from game import Game2v2

game = Game2v2()
game.show_cards()

id = 0

last_play_id = -1

while(True):
    if last_play_id==id:
        game.new_turn()
    print("trun of player", id)
    cards = game.see_cards(id)
    print("cards of player", id, ":", cards)
    if game.check_play(id):
        print("can play a card")
        card = game.play_card(id)
        print("play card: ", card)
        last_play_id = id
    if game.check_win()>-1:
        break
    id = id+1 if id<3 else 0

print("winner: player", id)