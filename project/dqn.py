
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
import numpy as np
import random
from collections import deque

class dqnAgent():
    def __init__(self, n_actions, learning_rate=0.01, discount=0.99, epsilon=0.1):
        self.learning_rate = learning_rate
        self.discount = discount
        self.n_actions = n_actions
        self.epsilon = epsilon
        self.memory = deque(maxlen=2000)
        self.model = self._createModel(n_actions)

    def act(self, observation):
        # explore...
        if np.random.rand() <= self.epsilon:
            return np.random.randint(self.n_actions)
        # exploit...
        return np.argmax(self.model.predict(observation)[0])

    def remember(self, s1, a, r, s2, done):
        self.memory.append((s1,a,r,s2, done))

    def replay(self, n):
        episodes = random.sample(self.memory, n)

        for s1, a, r, s2, done in episodes:
            if not done:
                r2 = r + self.discount * np.amax(self.model.predict(s2)[0])
            else:
                r2 = r
            # get the predicition for the state...
            prediction = self.model.predict(s1) 
            prediction[0][a] = r2
            self.model.fit(s1, prediction, epochs=1, verbose=0)


    def _createModel(self, n_actions):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=8, strides=4, activation='relu', input_shape=(88,88,1)))
        model.add(Conv2D(64, kernel_size=4, strides=2, activation='relu'))
        model.add(Conv2D(64, kernel_size=3, strides=1, activation='relu'))
        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dense(n_actions, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model