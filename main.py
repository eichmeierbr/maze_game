from mars import *
from mars_action import *
from maze import *
from player import *
from custom_player import *

# Pick Player
play = player()
# play = custom_player(block_coding=True)
# play = custom_player()

# Pick Game
# gam = maze_game(map_file='maze_hard.csv')
# gam = mars_game(random_start=False)
gam = mars_action_game(random_start=True)

# Play Game
gam.play_game(play)