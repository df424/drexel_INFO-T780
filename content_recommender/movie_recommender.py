
import numpy as np

# Compare two genres for an entire column X which returns 1 if X is 1 and x is 1
# or 0 otherwise.
def genreCompare(X, x):
    # if x is 0 then we don't care about any match at all.
    if x == 0:
        return np.zeros(X.shape)
    # otherwise do the binary compare..
    return (X == x).astype(int)

# Do a binary comparison on an entire column and a single value.
def binaryCompare(X, x):
    return (X == x).astype(int)

# computes the absolute difference normalized by the range and subtracts it from 1.
# in otherwords if two values exactly match they get a value of 1, they get 0
# if they are on oposite ends of the range.
def absDifference(X, x):
    return 1-np.abs(X-x)/X.max()

#This class represents a movie recommender once it is given all the data
# it can compute the k nearest neighbor using the similarity functions.
# and the weight vector.
class MovieRecommenderSystem(object):
    # this is everything we need to make a recommendation.
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

        # find the maximum values.
        max_vals = np.argpartition(similarity_factor, -n_recommendations)[-n_recommendations:]
        max_vals = max_vals[np.argsort(-similarity_factor[max_vals])]

        # return the data from the Y vector.
        return [self.Y[v] for v in max_vals]

        