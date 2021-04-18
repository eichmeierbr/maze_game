import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from game import *

class maze_game(game):
    def __init__(self, map_file='maze_easy.csv'):
        self.img = np.loadtxt(map_file,delimiter=',')
        
        self.map = self.make_map()
        self.map_size = self.map.shape

        super().__init__()

        self.show_img()




    def make_map(self):
        temp = np.flipud(self.img).T
        return temp
