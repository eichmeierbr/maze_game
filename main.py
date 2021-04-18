import numpy as np
import matplotlib.pyplot as plt

from mars import *
from maze import *
from player import *

# Pick Player
player = player()

# Pick Game
gam = maze_game()
# gam = mars_game()

# Play Game
gam.play_game(player)