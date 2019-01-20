import gym
from policy import Policy

def simulate_episode():
    env = gym.make('MountainCar-v0')
    env._max_episode_steps = 500
    total_reward = 0
    for i_episode in range(1):
        observation = env.reset()
        for t in range(1000):
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            total_reward += reward
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break
        print("Total reward: {}".format(total_reward))

def test_policy():
    policy = Policy(epsilon=0.5, verbose=True)
    print(policy.Q)
    print('For state 0')
    for i in range(10):
        print(policy.get_action_eps_greedy(0))
    print('For state 1')
    for i in range(10):
        print(policy.get_action_eps_greedy(1))

test_policy()