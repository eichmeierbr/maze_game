import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

plt.ion()

class game:
    def __init__(self):
        if not hasattr(self,'img'):
            self.img = plt.imread("mars.jpg")
        if not hasattr(self,'map_size'):
            self.map_size = [15,12]
        if not hasattr(self,'map'):
            self.map = self.make_map()
       
        self.fig, self.ax = plt.subplots()

        self.valid_actions = ['U', 'D', 'L', 'R']
        self.last_act = ''

        self.robot_pos = np.array([2,1])
        self.robot_img = OffsetImage(plt.imread("robot.png"), zoom=.04)

        self.goal_pos = np.array([1,4])
        self.goal_img = OffsetImage(plt.imread("goal.png"), zoom=.03)

        self.plot_offset = [.5,.5]

        self.goal_text = 'Navigate to the Goal'
        self.action_text = 'Move Robotr: U:^, D:v, L:<, R:>'
        self.success_text= 'WOOHOO! Robot reached the goal!'
        self.obstacle_text= 'Collision'
        self.invalid_in_txt = 'Invalid input received'
        self.show_invalid_text = False
        self.show_success_text = False
        self.show_obstacle_text = False


    def play_game(self, player):
        while True:
            self.show_img()

            act = player.act(self)
            self.last_act = act
            print(act)

            temp = self.robot_pos + 0
            if act in self.valid_actions:
                ## Get action
                if act == 'U':
                    temp[1] +=1
                elif act == 'D':
                    temp[1] -=1
                elif act == 'R':
                    temp[0] +=1
                elif act == 'L':
                    temp[0] -=1
            else:
                self.show_invalid_text = True

            

            ## Check for collision
            if self.map[temp[0], temp[1]] == 0:
                self.robot_pos = temp[:]
            else:
                self.show_obstacle_text = True
                print(self.obstacle_text)

            ## Check end condition
            if np.allclose(self.robot_pos, self.goal_pos):
                self.show_success_text = True
                print(self.success_text)
                self.show_img()
                plt.pause(5)
                return


    def make_map(self):
        temp = np.ones([self.map_size[0]+1, self.map_size[1]+1])
        temp[1:-1,1:-1] = 0
        temp[7:9,6:9] = 1
        temp[11:14,5:11] = 1
        temp[10,6:10] = 1
        return temp


    def show_img(self):
        self.ax.cla()

        # Plot image
        if len(self.img.shape) == 2:
            self.ax.imshow(self.img, extent=[0, self.map_size[0], 0, self.map_size[1]], cmap='Greys')
        else:
            self.ax.imshow(self.img, extent=[0, self.map_size[0], 0, self.map_size[1]])

        # Plot base
        x, y = self.goal_pos
        dx, dy = self.plot_offset
        ab = AnnotationBbox(self.goal_img, (x+dx, y+dy), frameon=False)
        self.ax.add_artist(ab)

        # Plot rover
        x, y = self.robot_pos
        ab = AnnotationBbox(self.robot_img, (x+dx, y+dy), frameon=False)
        self.ax.add_artist(ab)

        ## Draw Title Text
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

        title = self.goal_text + '\n' + self.action_text + '\n' + extra
        plt.title(title)

        ## Draw Action Text
        plt.gcf().text(.88, .96,'Action:', fontsize=12)
        plt.gcf().text(.92, .92,self.last_act, fontsize=12)

        plt.draw()
        plt.pause(.01)

        ## Remove Texts
        self.fig.texts = []