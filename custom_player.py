import numpy as np
from game.game import *
from players.player import *
from game.mars_action import *
from players.example_players import *

''' 
Here are some things you can do:

You can only move up, down, left, or right at any turn

Move up:        self.moveUp()
Move down:      self.moveDown()
Move left:      self.moveLeft()
Move right:     self.moveRight()

You can also check to see if you can move a certain direction

        self.canMoveUp()
        self.canMoveDown()
        self.canMoveLeft()
        self.canMoveRight()

    Example:

    if self.canMoveUp():
        self.moveUp()

You can also check what your last move was (which direction are you looking):

        direction = self.direction
        This will give you 'u', 'l', 'd', or 'r'

In the Mars Action game there is also an action to pick up the Martian:

Can you perform the action:             self.canDoAction()
Perorm action (pick up the martian):    self.doAction()
Check if you need to do the action:     self.needAction()

'''

class CustomPlayer(Player):
    def __init__(self, block_coding=False):
        super().__init__(block_coding=block_coding)


    def custom_action(self, robot_x, robot_y, goal_x, goal_y, Map):

        if hasattr(self.scene, 'martian_pos'):
            martian_x, martian_y = self.scene.martian_pos

        ### Start your code here
        left_right_up_down(robot_x, robot_y, goal_x, goal_y, self)
        ### End your code here