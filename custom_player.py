import numpy as np
from game import *
from player import *
from mars_action import *

''' 
Here are some things you can do:

You can only move up, down, left, or right at any turn

Move up:        action = self.moveUp()
Move down:      action = self.moveDown()
Move left:      action = self.moveLeft()
Move right:     action = self.moveRight()

You can also check to see if you can move a certain direction

        self.canMoveUp()
        self.canMoveDown()
        self.canMoveLeft()
        self.canMoveRight()

    Example:

    if self.canMoveUp():
        action = self.moveUp()

You can also check what your last move was (which direction are you looking):

        direction = self.direction
        This will give you 'u', 'l', 'd', or 'r'

In the Mars Action game there is also an action to pick up the Martian:

Can you perform the action:             self.canDoAction()
Perorm action (pick up the martian):    action = self.doAction()
Check if you need to do the action:     self.needAction()

'''

class custom_player(player):
    def __init__(self, block_coding=False):
        super().__init__()
        self.block_coding = block_coding


    def custom_action(self, robot_x, robot_y, goal_x, goal_y, Map):

        if hasattr(self.scene, 'martian_pos'):
            martian_x, martian_y = self.scene.martian_pos

        ### Start your code here

        ## Move left and right
        if goal_y > robot_y  and self.canMoveUp():
            self.moveUp()
        elif goal_y < robot_y and self.canMoveDown(): 
            self.moveDown()


        ## Move up and down
        elif goal_x > robot_x and self.canMoveRight():
            self.moveRight()
        else:
            self.moveLeft()

        # self.moveLeft(4)


        ### End your code here