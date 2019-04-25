

# area constants
LIVING_ROOM = 'living_room'
KITCHEN = 'kitchen'
CUPBOARD = 'cupboard'
FRIDGE = 'fridge'

#door constants
KITCHEN_DOOR = 'kitchen door'
FRIDGE_DOOR = 'fridge door'
CUPBOARD_DOOR = 'cupboard door'

#entity constants
ROBOT = 'robot'
PERSON = 'person'
GLASS = 'glass'
SODA = 'soda'
NONE = 'none'

# states
LOCATION = 'location'
HOLDS = 'holds'
CLOSED = 'closed'
OPENED = 'opened'

class Move(object):
    def __init__(self, entity, from_loc, to_loc, door):
        self.entity = entity
        self.from_loc = from_loc
        self.to_loc = to_loc
        self.door = door

    def PreconditionsSatisifed(self, state):
        return state[self.entity][LOCATION] == self.from_loc and \
               state[self.door] == OPENED

    def Apply(self, state):
        # move the entity...
        state[self.entity][LOCATION] = self.to_loc
        # if the entity is holding something move that too.
        if state[self.entity][HOLDS] != NONE:
            state[state[self.entity][HOLDS]][LOCATION] = self.to_loc

class ManipulateDoor(object):
    def __init__(self, entity, door, locations, from_state, to_state):
        self.entity = entity
        self.from_state = from_state
        self.to_state = to_state
        self.locations = locations
        self.door = door

    def PreconditionsSatisifed(self, state):
        # can't maniuplate a door that is already in the state we want it in...
        if state[self.door] == self.to_state:
            return False
        
        # can't open a door if the entity isn't in one of the locations
        if state[self.entity][LOCATION] not in self.locations:
            return False

        # I guess we can open it then.
        return True
    
    def Apply(self, state):
        state[self.door] = self.to_state

class Give(object):
    def __init__(self, from_entity, to_entity):
        self.from_entity = from_entity
        self.to_entity = to_entity

    def PreconditionsSatisifed(self, state):
        # Can't give something to someone if we aren't in the same location.
        if state[self.from_entity][LOCATION] != state[self.to_entity][LOCATION]:
            return False
        
        # Can't give something to someone if we aren't holding anything.
        if state[self.from_entity][HOLDS] == NONE:
            return False

        # or if they are holding something else...
        if state[self.to_entity][HOLDS] != NONE:
            return False
        
        return True
    
    def Apply(self, state):
        # transfer the entity
        state[self.to_entity][HOLDS] = state[self.from_entity][HOLDS]
        state[self.from_entity][HOLDS] = NONE


class Take(object):
    def __init__(self, taker_entity, target_entity):
        self.taker_entity = taker_entity
        self.target_entity = target_entity

    def PreconditionsSatisifed(self, state):
        # can't take something if we aren't in the same location.
        if state[self.taker_entity][LOCATION] != state[self.target_entity][LOCATION]:
            return False
        
    def Apply(self, state):
        state[self.taker_entity][HOLDS] = self.target_entity


if __name__ == '__main__':
    start_state = {ROBOT:{LOCATION:LIVING_ROOM, HOLDS:NONE},
                   PERSON:{LOCATION:LIVING_ROOM, HOLDS:NONE},
                   GLASS:{LOCATION:CUPBOARD, HOLDS:NONE},
                   SODA:{LOCATION:FRIDGE, HOLDS:NONE},
                   KITCHEN_DOOR:CLOSED,
                   FRIDGE_DOOR:CLOSED, 
                   CUPBOARD_DOOR:CLOSED}

    goal_state =  {ROBOT:{LOCATION:LIVING_ROOM, HOLDS:NONE},
                   PERSON:{LOCATION:LIVING_ROOM, HOLDS:GLASS},
                   GLASS:{LOCATION:LIVING_ROOM, HOLDS:SODA},
                   SODA:{LOCATION:LIVING_ROOM, HOLDS:NONE},
                   KITCHEN_DOOR:CLOSED,
                   FRIDGE_DOOR:CLOSED, 
                   CUPBOARD_DOOR:CLOSED}

    # create all the actions we can do...
    Actions = [
        Move(ROBOT, KITCHEN, LIVING_ROOM, KITCHEN_DOOR),
        Move(ROBOT, LIVING_ROOM, KITCHEN, KITCHEN_DOOR),
        Move(ROBOT, KITCHEN, FRIDGE, FRIDGE_DOOR),
        Move(ROBOT, FRIDGE, KITCHEN, FRIDGE_DOOR),
        Move(ROBOT, CUPBOARD, KITCHEN, CUPBOARD_DOOR),
        Move(ROBOT, KITCHEN, CUPBOARD, CUPBOARD_DOOR),
        ManipulateDoor(ROBOT, KITCHEN_DOOR, [KITCHEN, LIVING_ROOM], OPENED, CLOSED),
        ManipulateDoor(ROBOT, KITCHEN_DOOR, [KITCHEN, LIVING_ROOM], CLOSED, OPENED),
        ManipulateDoor(ROBOT, FRIDGE_DOOR, [FRIDGE, KITCHEN], OPENED, CLOSED),
        ManipulateDoor(ROBOT, FRIDGE_DOOR, [FRIDGE, KITCHEN], CLOSED, OPENED),
        ManipulateDoor(ROBOT, CUPBOARD_DOOR, [CUPBOARD, KITCHEN], OPENED, CLOSED),
        ManipulateDoor(ROBOT, CUPBOARD_DOOR, [CUPBOARD, KITCHEN], CLOSED, OPENED),
    ]