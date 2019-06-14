
import gym
import numpy as np
import scipy.misc
import sys
from preprocess import scaleImg, toGrayScale
from dqn import createModel

def main():
    env = gym.make("Pong-v0")
    observation = env.reset()
    done = False

    dqn_model = createModel(3)

    while not done:
        env.render()
        observation, reward, done, info = env.step(3)

        # reduce the observation to the gameplay area of the screen and preprocess the image...
        observation = toGrayScale(scaleImg(observation[34:194])).reshape((-1, 88, 88, 1))
        dqn_model.fit(observation, np.array([[0.5, 0.5, 0.5]]), epochs=1)

        # calculate the location of the ball...
        #core_screen = core_screen - 236
        #ball_pix = np.argwhere(np.abs(core_screen).sum(axis=2) == 0)
        #ball_pix.mean(axis=0)

if __name__=='__main__':
    main()

