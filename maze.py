import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from game import *

plt.ion()

class maze_game(game):
    def __init__(self, map='maze_easy.csv'):
        self.img = np.loadtxt('maze_easy.csv',delimiter=',')
        
        self.map = self.make_map()
        self.map_size = self.map.shape

        self.fig, self.ax = plt.subplots()

        self.valid_actions = ['U', 'D', 'L', 'R']
        self.last_act = ''

        self.robot_pos = np.array([2,1])
        self.robot_img = OffsetImage(plt.imread("robot.png"), zoom=.04)

        self.goal_pos = np.array([1,4])
        self.goal_img = OffsetImage(plt.imread("goal.png"), zoom=.03)

        self.plot_offset = [.5,.5]

        self.goal_text = 'Navigate to the Goal'
        self.action_text = 'Move Robot: U:^, D:v, L:<, R:>'
        self.success_text= 'WOOHOO! Rover reached the Goal!'
        self.obstacle_text= 'You hit the wall!'
        self.invalid_in_txt = 'Invalid input received'
        self.show_invalid_text = False
        self.show_success_text = False
        self.show_obstacle_text = False
        self.show_img()




    def make_map(self):
        temp = np.flipud(self.img).T
        return temp
