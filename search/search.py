
def BFS(start, goal):
    closed = {}
    frontier = [start]
    closed[start.getHash()] = None

    # check the degenerate case.
    if start.equals(goal):
        return [start, goal]

    while len(frontier) > 0:
        # get the next node to expand.
        current = frontier.pop()
        # expand it
        actions = current.getMoves()

        # process the children.
        for a in actions:
            new_state = current.applyMove(a)

            # if child not encountered before.
            if new_state.hash not in closed:
                # add it to the closed list and frontier storing the parent state.
                # and the action we came here by.
                closed[new_state.hash] = (a, current)
                frontier.insert(0, new_state)

                # check if we found the solution.
                if new_state.equals(goal):
                    return computePath(closed, new_state)
    return None

def computePath(closed, goal):
    rv = [(None, goal)]
    parent = closed[goal.getHash()]
    while parent:
        rv.insert(0, parent)
        parent = closed[parent[1].getHash()]
    return rv