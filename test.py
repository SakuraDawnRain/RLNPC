from env import GameEnv

env = GameEnv()

termination = False

max_round = 100

while(max_round>0):
    max_round = max_round-1

    player_id, can_play, observation, termination = env.last()

    if termination:
        env.report()
        break
    
    if can_play:
        action = True
    
    env.step(action)

