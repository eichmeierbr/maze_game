import numpy as np
from game.mars import *
from game.mars_action import *
from game.maze import *
from players.player import *

from game.game import *
from players.player import *
from game.mars_action import *
from players.example_players import *

from IPython.display import HTML

def custom_robot(robot_x, robot_y, goal_x, goal_y, robot, map):
    """ 
    Here are some things you can do:

    You can only move up, down, left, or right at any turn

    Move up:        self.moveUp()
    Move down:      self.moveDown()
    Move left:      self.moveLeft()
    Move right:     self.moveRight()

    You can also check to see if you can move a certain direction

            robot.canMoveUp()
            robot.canMoveDown()
            robot.canMoveLeft()
            robot.canMoveRight()

        Example:

        if map.canMoveUp():
            robot.moveUp()

    You can also check what your last move was (which direction are you looking):

            direction = robot.direction
            This will give you 'u', 'l', 'd', or 'r'

    In the Mars Action game there is also an action to pick up the Martian:

    Can you perform the action:             robot.canDoAction()
    Perorm action (pick up the martian):    robot.doAction()
    Check if you need to do the action:     robot.needAction()
    """
    robot.useCheat(reuse=True)


def run_game():
    # Pick Player
    play = Player(custom_robot, block_coding=False)

    # Pick Game
    # gam = MazeGame(map_file='mazes/maze_hard.csv')
    gam = MarsGame(random_start=False)
    # gam = MarsActionGame(random_start=True)

    gam.player = play

    # Play Game
    gam.play_game_loop()

    return gam

if __name__=="__main__":
    gam = run_game()

    gam.anim.save('robot.gif', writer="pillow", fps=5)