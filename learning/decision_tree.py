
import numpy as np

def createTree(tree, X, Y, indices, get_idx_fx):
    idx = get_idx_fx(indices)
    # if the function didn't remove the index do it now.
    if idx in indices:
        indices.remove(idx)

    # partition on the indices...
    partitions = partition(X,Y, idx)

    # now for each partition...
    for p in partitions:
        x, y = p
        # if it happened that this partition only contains leaf nodes...
        if(np.all(y==y[0])):
            print("ALL!")

def partition(X, Y, i):
    """Partitions the set X with labels Y into n different sets where n is the cardinality of row i."""
    choices = np.unique(X[:,i])
    rv = []

    for c in choices:
        indices = np.argwhere(X[:,i] == c)
        rv.append((X[indices,:], Y[indices]))

    return rv

def inOrderSelector(indices):
    return indices[0]