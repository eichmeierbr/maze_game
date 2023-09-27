import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from game.game import *

class MarsGame(Game):
    def __init__(self, random_start=False, robot_start=np.array([10,1]), goal_start=np.array([2,9])
):
        self.img = plt.imread("images/mars.jpg")
        self.map_size = [15,12]
        self.map = self.make_map()

        super().__init__()

        self.valid_actions = ['U', 'D', 'L', 'R', '_']

        if random_start:
            self.robot_pos, self.goal_pos = self.random_starts()
        else:
            self.robot_pos = robot_start
            self.goal_pos = goal_start

        self.robot_img = OffsetImage(plt.imread("images/rover2.png"), zoom=.15)
        self.goal_img = OffsetImage(plt.imread("images/base.png"), zoom=.25)

        self.plot_offset = [0,0]

        self.goal_text = 'Navigate to the Mars Base'
        self.action_text = 'Move Rover: W:^, S:v, A:<, D:>'
        self.success_text= 'WOOHOO! Rover reached the base!'
        self.obstacle_text= 'Crater Detected'
        self.invalid_in_txt = 'Invalid input received'

        self.show_img()


    def random_starts(self):

        val = 1
        while val:
            x = np.random.randint(0, self.map_size[0])
            y = np.random.randint(0, self.map_size[1])
            val = self.map[x, y]

        # robot_pose = np.array([13,1])
        robot_pose = np.array([x,y])

        val = 1
        while val:
            x = np.random.randint(0, self.map_size[0])
            y = np.random.randint(0, self.map_size[1])
            val = self.map[x, y]
            diff = robot_pose - [x,y]
            val = val or np.sum(np.abs(diff)) < 8

        goal_pose = np.array([x, y])

        a=3
        return robot_pose, goal_pose



    def make_map(self):
        temp = np.ones([self.map_size[0]+1, self.map_size[1]+1])
        temp[1:-1,1:-1] = 0
        temp[7:9,6:9] = 1
        temp[11:14,5:11] = 1
        temp[10,6:10] = 1
        return temp