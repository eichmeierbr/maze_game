from game.mars import *
from game.mars_action import *
from game.maze import *
from players.player import *
from custom_player import *

def run_game():
    # Pick Player
    play = Player()
    # play = CustomPlayer(block_coding=False)
    # play = CustomPlayer()

    # Pick Game
    # gam = MazeGame(map_file='mazes/maze_hard.csv')
    gam = MarsGame(random_start=False)
    # gam = MarsActionGame(random_start=True)

    # Play Game
    gam.play_game(play)


if __name__=="__main__":
    run_game()