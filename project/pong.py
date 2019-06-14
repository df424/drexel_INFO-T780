
import gym
import numpy as np
import scipy.misc
import sys
from preprocess import scaleImg, toGrayScale
from dqn import dqnAgent

def main():
    env = gym.make("Pong-v0")
    agent = dqnAgent(6) 

    for i in range(1000000):
        print(i)
        done = False
        current_observation = env.reset()
        current_observation = toGrayScale(scaleImg(current_observation[34:194])).reshape((-1, 88, 88, 1))
        while not done:
            #if i % 100 == 0:
            env.render()

            # act...
            a = agent.act(current_observation)

            # update environment...
            next_observation, reward, done, info = env.step(a)

            # process the observation
            next_observation = toGrayScale(scaleImg(next_observation[34:194])).reshape((-1, 88, 88, 1))

            # update the agent's memory.
            agent.remember(current_observation, a, reward, next_observation, done)

            # save the observation for the next state.
            current_observation = next_observation

            # calculate the location of the ball...
            #core_screen = core_screen - 236
            #ball_pix = np.argwhere(np.abs(core_screen).sum(axis=2) == 0)
            #ball_pix.mean(axis=0)
        agent.replay(32)

if __name__=='__main__':
    main()

