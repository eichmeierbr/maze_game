import numpy as np
from pynput import keyboard
from game import *

    

class player:
    def __init__(self):
        self.direction = 'u'
        self.robot_x = 0
        self.robot_y = 0
        self.goal_x = 0
        self.goal_y = 0
        self.map = 0
        self.scene = None
        pass


    def doAction(self):
        return 'a'

    def moveUp(self):
        return 'u'

    def moveDown(self):
        return 'd'

    def moveLeft(self):
        return 'l'

    def moveRight(self):
        return 'r'

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
        action = self.custom_action(robot_x, robot_y, goal_x, goal_y, self.map)

        self.set_direction(action)
        return action[0].upper()


    def custom_action(self, robot_x, robot_y, goal_x, goal_y, Map):
        action = '_'
        
        if self.canDoAction():
            action = self.doAction()
            return action
        
        while action[0] == '_':
            with keyboard.Events() as events:
                event = events.get(1e6)
                if hasattr(event.key,'char'):
                    action = event.key.char
        
        return action

