
from search import BFS
from means_end import *
from puzzle import Puzzle
import argparse
import numpy as np

def means_end(args):
    start_state = MeansEndState({ROBOT:{LOCATION:LIVING_ROOM, HOLDS:NONE},
                                PERSON:{LOCATION:LIVING_ROOM, HOLDS:NONE},
                                GLASS:{LOCATION:CUPBOARD, HOLDS:NONE},
                                SODA:{LOCATION:FRIDGE, HOLDS:NONE},
                                KITCHEN_DOOR:CLOSED,
                                FRIDGE_DOOR:CLOSED, 
                                CUPBOARD_DOOR:CLOSED})

    goal_state =  MeansEndState({ROBOT:{LOCATION:LIVING_ROOM, HOLDS:NONE},
                                PERSON:{LOCATION:LIVING_ROOM, HOLDS:GLASS},
                                GLASS:{LOCATION:LIVING_ROOM, HOLDS:SODA},
                                SODA:{LOCATION:LIVING_ROOM, HOLDS:NONE},
                                KITCHEN_DOOR:CLOSED,
                                FRIDGE_DOOR:CLOSED, 
                                CUPBOARD_DOOR:CLOSED})

    path = BFS(start_state, goal_state)

    for s in path:
        if s[0]:
            print(s[0])

def puzzle(args):
    start = Puzzle(np.array([4, 3, 6, 8, 2, 7, 5, 1, 0]))
    goal  = Puzzle(np.array([8, 1, 2, 7, 0, 3, 6, 5, 4]))

    path = BFS(start, goal)

    for s in path:
        print(s[1].board.reshape((3,3)))
        if s[0]:
            print("ACTION: ", s[0])

if __name__ == '__main__':
    COMMANDS = {'puzzle':puzzle, 'means-end':means_end}
    parser = argparse.ArgumentParser(description='Run search procedures for assignment 1')
    parser.add_argument('command', choices=COMMANDS.keys(), 
                        help="You must pass one of the following commands to run: " + str(COMMANDS.keys()))
    args = parser.parse_args()

    # get the command from the map.
    command = COMMANDS[args.command]
    # call it with the arguments.
    command(args)