import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

plt.ion()

class mars_game:
    def __init__(self):
        self.map_size = [15,12]
        self.map = self.make_map()
        self.fig, self.ax = plt.subplots()
        self.img = plt.imread("mars.jpg")

        self.valid_actions = ['U', 'D', 'L', 'R']
        self.last_act = ''

        self.robot_pos = np.array([10,1])
        self.robot_img = OffsetImage(plt.imread("rover2.png"), zoom=.15)

        self.goal_pos = np.array([2,9])
        self.goal_img = OffsetImage(plt.imread("base.png"), zoom=.25)

        self.plot_offset = [0,0]

        self.goal_text = 'Navigate to the Mars Base'
        self.action_text = 'Move Rover: U:^, D:v, L:<, R:>'
        self.success_text= 'WOOHOO! Rover reached the base!'
        self.obstacle_text= 'Crater Detected'
        self.invalid_in_txt = 'Invalid input received'
        self.show_invalid_text = False
        self.show_success_text = False
        self.show_obstacle_text = False
        self.show_img()


    def play_game(self, player):
        while True:
            self.show_img()

            act = player.act(self)
            self.last_act = act
            print(act)

            if act in self.valid_actions:
                ## Get action
                temp = self.robot_pos + 0
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
        self.ax.imshow(self.img, extent=[0, self.map_size[0], 0, self.map_size[1]])

        # Plot base
        x, y = self.goal_pos
        ab = AnnotationBbox(self.goal_img, (x, y), frameon=False)
        self.ax.add_artist(ab)

        # Plot rover
        x, y = self.robot_pos
        ab = AnnotationBbox(self.robot_img, (x, y), frameon=False)
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