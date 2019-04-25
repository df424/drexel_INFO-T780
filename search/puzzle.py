import numpy as np
import math

class Puzzle:
    def __init__(self, board):
        self.board = np.copy(board)
        self.hash = self.getHash()

    def equals(self, other):
        return np.all(self.board == other.board)

    def getMoves(self):
        rv = []
        #get index of 0.
        idx = np.argmin(self.board)

        # we can move up if idx > 2
        if(idx > 2):
            rv.append((idx,idx-3))
        # we can move down if idx < 6
        if(idx < 6):
            rv.append((idx, idx+3))
        # we can move left if idx is not 0, 3, or 6
        if(idx % 3 != 0):
            rv.append((idx, idx-1))
        # we can move right if idx is not 2, 5, or 8
        if(idx % 3 != 2):
            rv.append((idx, idx+1))

        return rv

    def applyMove(self, move):
        rv = Puzzle(self.board)
        tmp = rv.board[move[0]]
        rv.board[move[0]] = rv.board[move[1]]
        rv.board[move[1]] = tmp
        return rv
    
    def applyMoves(self, moves):
        rv = []
        for move in moves:
            rv.append(self.applyMove(move))
        return rv

    def getChildStates(self):
        return self.applyMoves(self.getMoves())

    def getHash(self):
        rv = 0
        base = len(self.board)
        for i, b in enumerate(self.board):
            rv = rv + math.pow(base, i) * b
        return rv



