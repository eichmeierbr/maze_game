from player import *

def left_right_up_down(robot_x, goal_x, robot_y, goal_y):
    ## This function will align itself left-right with the goal.
    ## Then it will move up-down to the goal

    if robot_x > goal_x:
        action = moveLeft()

    elif robot_x < goal_x:
        action = moveRight()
    
    elif robot_y < goal_y:
        action = moveUp()
    
    else:
        action = moveDown()


def followWall(robot_x, goal_x, robot_y, goal_y):
    ## This function always follows the right wall

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