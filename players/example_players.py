def left_right_up_down(robot_x, robot_y, goal_x, goal_y, robot, map):
    ## This function will align itrobot left-right with the goal.
    ## Then it will move up-down to the goal

    if robot_x > goal_x:
        robot.moveLeft()

    elif robot_x < goal_x:
        robot.moveRight()
    
    elif robot_y < goal_y:
        robot.moveUp()
    
    else:
        robot.moveDown()


def followWall(robot_x, robot_y, goal_x, goal_y, robot, map):
    ## This function always follows the right wall

    # Looking up
    if robot.direction == 'u':
        if robot.canMoveRight():
            return robot.moveRight()
        elif robot.canMoveUp():
            return robot.moveUp()
        elif robot.canMoveLeft():
            return robot.moveLeft()
        else:
            return robot.moveDown()

    # Looking Right
    if robot.direction == 'r':
        if robot.canMoveDown():
            return robot.moveDown()
        elif robot.canMoveRight():
            return robot.moveRight()
        elif robot.canMoveUp():
            return robot.moveUp()
        else:
            return robot.moveLeft()

    # Looking Down
    if robot.direction == 'd':
        if robot.canMoveLeft():
            return robot.moveLeft()
        elif robot.canMoveDown():
            return robot.moveDown()
        elif robot.canMoveRight():
            return robot.moveRight()
        else: # robot.canMoveUp():
            return robot.moveUp()

    # Looking Left
    if robot.direction == 'l':
        if robot.canMoveUp():
            return robot.moveUp()
        elif robot.canMoveLeft():
            return robot.moveLeft()
        elif robot.canMoveDown():
            return robot.moveDown()
        else:
            return robot.moveRight()