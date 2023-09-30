import numpy as np
from game.mars import *
from game.mars_action import *
from game.maze import *
from players.player import *
from custom_player import *

from game.game import *
from players.player import *
from game.mars_action import *
from players.example_players import *


def custom_robot(robot_x, robot_y, goal_x, goal_y, robot, map):
    """ 
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
    """
    if robot_x > goal_x:
        robot.moveLeft()

    elif robot_x < goal_x:
        robot.moveRight()
    
    elif robot_y < goal_y:
        robot.moveUp()
    
    else:
        robot.moveDown()


def run_game():
    # Pick Player
    play = Player(left_right_up_down, block_coding=False)

    # Pick Game
    # gam = MazeGame(map_file='mazes/maze_hard.csv')
    gam = MarsGame(random_start=False)
    # gam = MarsActionGame(random_start=True)

    # Play Game
    gam.play_game(play)


if __name__=="__main__":
    run_game()