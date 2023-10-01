import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.animation

plt.ion()

class Game:
    def __init__(self):
        if not hasattr(self,'img'):
            self.img = plt.imread("images/mars.jpg")
        if not hasattr(self,'map_size'):
            self.map_size = [15,12]
        if not hasattr(self,'map'):
            self.map = self.make_map()
       
        self.fig, self.ax = plt.subplots()

        self.valid_actions = ['U', 'D', 'L', 'R', '_']
        self.last_act = ''

        self.robot_pos = np.array([2,1])
        self.last_robot_pos = np.copy(self.robot_pos)
        self.goal_pos = np.array([1,4])

        self.robot_img = OffsetImage(plt.imread("images/robot.png"), zoom=.04)
        self.goal_img = OffsetImage(plt.imread("images/goal.png"), zoom=.03)

        self.plot_offset = [.5,.5]
        self.turn = 0
        self.max_turns = 50

        self.stuck_count=0
        self.max_stuck = 10

        self.goal_text = 'Navigate to the Goal'
        self.action_text = 'Move Robot: W:^, S:v, A:<, D:>'
        self.success_text= 'WOOHOO! Robot reached the goal!'
        self.obstacle_text= 'Collision'
        self.invalid_in_txt = 'Invalid input received'
        self.stuck_text = 'Oh No, Robot Got Stuck! Try Again!'
        self.show_invalid_text = False
        self.show_success_text = False
        self.show_obstacle_text = False
        self.finished = False

        # plt.rcParams['keymap.save'].remove('s')    
        self.anim = matplotlib.animation.FuncAnimation(self.fig, self.play_game, frames=self.max_turns, interval=2, blit=False)


    def play_game_loop(self):
        while not self.play_game(0):
            pass

    def play_game(self, frame):
        if self.finished:
            return
        self.turn += 1

        self.show_img()

        ## Check end condition
        if self.checkEndCondition() or self.ran_out_of_time() or self.robot_got_stuck():
            self.show_success_text = True
            print(self.success_text)
            plt.pause(2)
            self.anim.event_source.stop()
            self.finished = True
            plt.close()
            return True

        act = self.player.act(self)
        self.last_act = act
        print(act)
        self.process_action(act)

        return False


    def ran_out_of_time(self):
        if self.turn > self.max_turns:
            self.success_text = "Ran out of time. Try again"
            return True
        return False

    def robot_got_stuck(self):
        if np.allclose(self.robot_pos, self.last_robot_pos):
            self.stuck_count +=1
        else:
            self.last_robot_pos = np.copy(self.robot_pos)
            self.stuck_count = 0
        
        if self.stuck_count > self.max_stuck:
            self.success_text = "Rover Got Stuck. Try Again"
            return True
        return False


    def process_action(self, act):
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

            self.custom_action(act)

    def custom_action(self, act):
        pass

    def checkEndCondition(self):
        return np.allclose(self.robot_pos, self.goal_pos)


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

        self.custom_plot()

        ## Draw Title Text
        title = self.goal_text + '\n' + self.action_text + '\n' + self.title_extra_txt()
        plt.title(title)

        ## Draw Action Text
        plt.gcf().text(.88, .96,'Action:', fontsize=12)
        plt.gcf().text(.92, .92,self.last_act, fontsize=12)


        plt.draw()
        plt.pause(.001)

        ## Remove Texts
        self.fig.texts = []

    def custom_plot(self):
        pass

    def title_extra_txt(self):
        extra = ''
        if self.show_invalid_text:
            extra = self.invalid_in_txt
            self.show_invalid_text = False
        elif self.show_success_text:
            extra = self.success_text
        elif self.show_obstacle_text:
            extra = self.obstacle_text
            self.show_obstacle_text = False
            self.show_success_text = False
        return extra
