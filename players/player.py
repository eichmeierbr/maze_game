import numpy as np
# from pynput import keyboard
from game.game import *
from players.a_star import *
    

class Player:
    def __init__(self, action_funciton=None, block_coding=False):
        self.direction = 'u'
        self.robot_x = 0
        self.robot_y = 0
        self.goal_x = 0
        self.goal_y = 0
        self.map = 0
        self.scene = None
        self.path = []
        self.block_coding = block_coding
        self.need_block_move = True
        self.actions = []
        if action_funciton is None:
            self.get_action = self.default_action
        else:
            self.get_action = action_funciton
        pass

    def followPath(self):
        # dict_map = {'[1,0]':'r', '[-1,0]':'l', '[0,-1]':'d', '[0,1]':'u'}
        if self.path[0][0] == 1: self.moveRight()
        if self.path[0][0] == -1: self.moveLeft()
        if self.path[0][1] == 1: self.moveUp()
        if self.path[0][1] == -1: self.moveDown()
        self.path = self.path[1:]



    def useCheat(self, reuse=False):
        if len(self.path) == 0 or not reuse:
            astar = AStar(self.scene.map, start=self.scene.robot_pos, goal=self.scene.goal_pos)
            self.path = astar.findPath(self.scene.robot_pos, self.scene.goal_pos)

        self.followPath()


    def doAction(self, count=1):
        self.actions += count*['a']

    def moveUp(self, count=1):
        self.actions += count*['u']

    def moveDown(self, count=1):
        self.actions += count*['d']

    def moveLeft(self, count=1):
        self.actions += count*['l']

    def moveRight(self, count=1):
        self.actions += count*['r']

    def canMoveUp(self):
        return not self.map[self.robot_x,self.robot_y+1]

    def canMoveDown(self):
        return not self.map[self.robot_x,self.robot_y-1]

    def canMoveLeft(self):
        return not self.map[self.robot_x-1,self.robot_y]

    def canMoveRight(self):
        return not self.map[self.robot_x+1,self.robot_y]

    def canDoAction(self):
        if hasattr(self.scene,'martian_pos') and not self.scene.has_martian:
            return np.allclose(self.scene.robot_pos, self.scene.martian_pos)
        return False

    def needAction(self):
        if hasattr(self.scene,'has_martian'):
            return self.scene.has_martian
        return False

    def set_direction(self,action):
        directs = ['u','l','d','r']
        if action in directs:
            self.direction = action


    def act(self, scene):

        self.scene = scene
        robot_x, robot_y = scene.robot_pos[:]
        goal_x, goal_y  = scene.goal_pos[:]

        self.robot_y = robot_y
        self.robot_x = robot_x
        self.goal_y = goal_y
        self.goal_x = goal_x
        self.map = np.copy(scene.map)

        action = '_'
        if (self.block_coding and self.need_block_move) or not self.block_coding:
            self.get_action(robot_x, robot_y, goal_x, goal_y, self, self.map)
            self.need_block_move = False

        if len(self.actions) > 0:
            action = self.actions[0]
            self.actions = self.actions[1:]

            self.set_direction(action)
        return action[0].upper()


    def default_action(self, robot_x, robot_y, goal_x, goal_y, robot, map):
        action = '_'
        
        if self.canDoAction():
            action = self.doAction()
            return action
        
        action = input()
        # while action[0] == '_':
            # with keyboard.Events() as events:
            #     event = events.get(1e6)
            #     if hasattr(event.key,'char'):
            #         action = event.key.char

        if action.lower()=='w':
            self.moveUp()
        elif action.lower()=='s':
            self.moveDown()
        elif action.lower()=='d':
            self.moveRight()
        elif action.lower()=='a':
            self.moveLeft()
        pass