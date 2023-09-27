import numpy as np
from queue import PriorityQueue
import copy

class Node():
    def __init__(self, x=0, y=0, path=[], cost=0):
        self.x = x
        self.y = y
        self.path = path
        self.cost = cost

    def __eq__(self, o: object) -> bool:
        return self.cost == o.cost

    def __lt__(self, o: object) -> bool:
        return self.cost < o.cost

    def __le__(self, o: object) -> bool:
        return self.cost <= o.cost
    def __gt__(self, o: object) -> bool:
        return self.cost > o.cost
    def __ge__(self, o: object) -> bool:
        return self.cost >= o.cost
        

class AStar():
    def __init__(self, map=None, start=None, goal=None):
        self.map = map
        self.visit_map = np.zeros_like(map)
        self.start = start
        self.goal  = goal
        self.pq = PriorityQueue()

    def getCost(self, node):
        c = node.cost + 1
        h = np.sum(np.abs([node.x-self.goal[0], node.y-self.goal[1]]))
        return c + h

    def processNode(self, node):
        ## Check error bounds
        if not 0 <= node.x < self.map.shape[0]:
            return
        if not 0 <= node.y < self.map.shape[1]:
            return

        ## Check if we have visited before
        if self.visit_map[node.x,node.y]:
            return

        ## Check if at goal
        if np.allclose(self.goal, [node.x, node.y]):
            return node.path
        
        self.visit_map[node.x, node.y] = 1

        node_left = copy.deepcopy(node)
        node_left.x -= 1
        if self.map[node_left.x, node_left.y] == 0:
            node_left.cost = self.getCost(node_left)
            node_left.path.append([-1,0])
            self.pq.put(node_left)

        node_right = copy.deepcopy(node)
        node_right.x += 1
        if self.map[node_right.x, node_right.y] == 0:
            node_right.path.append([1,0])
            node_right.cost = self.getCost(node_right)
            self.pq.put(node_right)

        node_up = copy.deepcopy(node)
        node_up.y += 1
        if self.map[node_up.x, node_up.y] == 0:
            node_up.path.append([0,1])
            node_up.cost = self.getCost(node_up)
            self.pq.put(node_up)
          
        node_down = copy.deepcopy(node)
        node_down.y -= 1
        if self.map[node_down.x, node_down.y] == 0:
            node_down.path.append([0,-1])
            node_down.cost = self.getCost(node_down)
            self.pq.put(node_down)

        return


    def findPath(self, start, goal):
        self.start = start
        self.goal = goal
        self.pq = PriorityQueue()

        firstNode = Node(start[0], start[1])
        self.pq.put(firstNode)

        while not self.pq.empty():
            node = self.pq.get()
            path = self.processNode(node)
            if not path == None:
                return path



if __name__ == "__main__":
    maze = np.loadtxt('mazes/maze_hard.csv', delimiter=',')

    robot_pos = np.array([1,48])
    goal_pos  = np.array([47,1])

    # robot_pos = np.array([2,1])
    # goal_pos = np.array([1,4])

    search = a_star(maze, robot_pos, goal_pos)

    path = search.findPath(robot_pos, goal_pos)
    print(path)
    a=3