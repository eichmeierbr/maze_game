import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from game import *

class mars_action_game(game):
    def __init__(self, random_start=False, robot_start=np.array([10,1]), goal_start=np.array([2,9]), martian_start=np.array([1,1])):
        super().__init__()

        self.valid_actions = ['U', 'D', 'L', 'R', 'A', '_']

        self.martian_pos = martian_start
        self.has_martian = False
        self.show_action_txt = False
        self.show_good_action_txt = False

        if random_start:
            self.robot_pos, self.goal_pos = self.random_starts()
        else:
            self.robot_pos = robot_start
            self.goal_pos = goal_start

        self.robot_img = OffsetImage(plt.imread("rover2.png"), zoom=.15)
        self.goal_img = OffsetImage(plt.imread("base.png"), zoom=.25)
        self.martian_img = OffsetImage(plt.imread("martian.png"), zoom=.03)

        self.plot_offset = [0,0]

        self.goal_text = 'Get the Martian to the Mars Base'
        self.action_text = 'Move Rover: U:^, D:v, L:<, R:>, A:act'
        self.success_text= 'WOOHOO! Rover reached the base!'
        self.obstacle_text= 'Crater Detected'
        self.invalid_in_txt = 'Invalid input received'
        self.need_action_txt = 'You still need the martian!!'
        self.good_action_txt = 'You picked up the martian!'

        self.show_img()


    def checkEndCondition(self):
        if np.allclose(self.robot_pos, self.goal_pos):
            if self.has_martian: return True
            # else:   print(self.need_action_txt)
            else:   self.show_action_txt = True
                 
        return False


    def random_starts(self):

        val = 1
        while val:
            x = np.random.randint(0, self.map_size[0])
            y = np.random.randint(0, self.map_size[1])
            val = self.map[x, y]

        robot_pose = np.array([x, y])

        val = 1
        while val:
            x = np.random.randint(0, self.map_size[0])
            y = np.random.randint(0, self.map_size[1])
            val = self.map[x, y]
            diff = robot_pose - [x,y]
            val = val or np.sum(diff) < 8

        goal_pose = np.array([x, y])

        return robot_pose, goal_pose


    def custom_action(self, act):
        if act == 'A' and np.allclose(self.robot_pos, self.martian_pos):
            if self.has_martian == False:
                self.show_good_action_txt = True
                self.has_martian = True

    def make_map(self):
        temp = np.ones([self.map_size[0]+1, self.map_size[1]+1])
        temp[1:-1,1:-1] = 0
        temp[7:9,6:9] = 1
        temp[11:14,5:11] = 1
        temp[10,6:10] = 1
        return temp


    def custom_plot(self):
        # Plot martian
        if self.has_martian:
            self.martian_pos = np.copy(self.robot_pos)

        x, y = self.martian_pos
        dx, dy = self.plot_offset
        ab = AnnotationBbox(self.martian_img, (x+dx, y+dy), frameon=False)
        self.ax.add_artist(ab)


    def title_extra_txt(self):
        extra = ''
        if self.show_invalid_text:
            extra = self.invalid_in_txt
            self.show_invalid_text = False
        elif self.show_obstacle_text:
            extra = self.obstacle_text
            self.show_obstacle_text = False
        elif self.show_success_text:
            extra = self.success_text
            self.show_success_text = False
        elif self.show_action_txt:
            extra = self.need_action_txt
            self.show_action_txt = False
        elif self.show_good_action_txt:
            extra = self.good_action_txt
            self.show_good_action_txt = False
        return extra
