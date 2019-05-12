
import numpy as np

def genreCompare(X, x):
    # if x is 0 then we don't care about any match at all.
    if x == 0:
        return np.zeros(X.shape)
    # otherwise do the binary compare..
    return (X == x).astype(int)

def binaryCompare(X, x):
    return (X == x).astype(int)

def absDifference(X, x):
    return 1-np.abs(X-x)/X.max()

class MovieRecommenderSystem(object):
    # What do i actually need to make the recommendation....
    # 1. The data cleaned and organized...
    # 2. Any normalization parameters to scale and transform between ML data and readable data.
    def __init__(self, X, Y, w, local_diffs):
        self.w = w
        self.X = X
        self.Y = Y
        self.local_diffs = local_diffs

    def getRecommendations(self, x, n_recommendations=10):
        # generate a matrix of local similarities for each row of data.
        similarities = np.zeros(self.X.shape)

        # for each column of data...
        for i in range(self.X.shape[1]):
            # compute the local similarity.
            similarities[:,i] = self.local_diffs[i](self.X[:,i], x[i])

        # We can use this and the weights to come up with a "similarity factor"
        similarity_factor = np.dot(similarities, self.w)

        max_vals = np.argpartition(similarity_factor, -n_recommendations)[-n_recommendations:]
        max_vals = max_vals[np.argsort(-similarity_factor[max_vals])]
        print([self.Y[v] for v in max_vals])

        