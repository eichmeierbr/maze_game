import numpy as np
import matplotlib.pyplot as plt

from mars import *
from maze import *
from player import *


player = player()
# gam = maze_game()
gam = mars_game()

gam.play_game(player)
a=3