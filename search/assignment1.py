
from search import BFS
from means_end import *

if __name__ == '__main__':
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
        print(s[0])

