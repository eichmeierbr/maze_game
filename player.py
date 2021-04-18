import numpy as np
from pynput import keyboard
from game import *

class player:
    def __init__(self):
        pass

    def act(self, scene):

        robot_position = scene.robot_pos[:]
        goal_position  = scene.goal_pos[:]


        action = '_'
        while action[0] == '_':
            with keyboard.Events() as events:
                event = events.get(1e6)
                if hasattr(event.key,'char'):
                    action = event.key.char

        return action[0].upper()