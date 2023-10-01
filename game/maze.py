import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from game.game import *

class MazeGame(Game):
    def __init__(self, map_file='mazes/maze_easy.csv'):
        self.img = np.loadtxt(map_file,delimiter=',')
        
        self.map = self.make_map()
        self.map_size = self.map.shape

        super().__init__()

        if map_file == 'mazes/maze_easy.csv':
            self.robot_pos = np.array([2,1])
            self.goal_pos = np.array([1,4])
        if map_file == 'mazes/maze_medium.csv':
            self.robot_pos = np.array([4,0])
            self.goal_pos = np.array([1,7])
        if map_file == 'mazes/maze_hard.csv':
            self.robot_pos = np.array([1,48])
            self.goal_pos = np.array([47,1])




    def make_map(self):
        temp = np.flipud(self.img).T
        return temp
