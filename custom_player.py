import numpy as np
from game import *
from player import *


class custom_player(player):
    def __init__(self):
        super().__init__()


    def custom_action(self, robot_x, robot_y, goal_x, goal_y, Map):
        action = '_'
        ### Start your code here

        # Looking up
        if self.direction == 'u':
            if self.canMoveRight():
                return self.moveRight()
            elif self.canMoveUp():
                return self.moveUp()
            elif self.canMoveLeft():
                return self.moveLeft()
            else:
                return self.moveDown()

        # Looking Right
        if self.direction == 'r':
            if self.canMoveDown():
                return self.moveDown()
            elif self.canMoveRight():
                return self.moveRight()
            elif self.canMoveUp():
                return self.moveUp()
            else:
                return self.moveLeft()

        # Looking Down
        if self.direction == 'd':
            if self.canMoveLeft():
                return self.moveLeft()
            elif self.canMoveDown():
                return self.moveDown()
            elif self.canMoveRight():
                return self.moveRight()
            else: # self.canMoveUp():
                return self.moveUp()

        # Looking Left
        if self.direction == 'l':
            if self.canMoveUp():
                return self.moveUp()
            elif self.canMoveLeft():
                return self.moveLeft()
            elif self.canMoveDown():
                return self.moveDown()
            else:
                return self.moveRight()

        ### End your code here
        return action