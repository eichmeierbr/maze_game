from mars import *
from mars_action import *
from maze import *
from player import *
from custom_player import *

# Pick Player
player = player()
# player = custom_player()

# Pick Game
# gam = maze_game(map_file='maze_medium.csv')
# gam = mars_game(random_start=False)
gam = mars_action_game(random_start=False)

# Play Game
gam.play_game(player)