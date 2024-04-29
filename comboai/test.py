import diambra.arena
import json
import os.path
from stable_baselines3 import A2C
from stable_baselines3.common.evaluation import evaluate_policy
from diambra.arena.stable_baselines3.make_sb3_env import make_sb3_env
from datetime import datetime

def prep(agent, env):
    try:
        # Load the trained agent
        # NOTE: if you have loading issue, you can pass `print_system_info=True`
        # to compare the system on which the agent was trained vs the current one
        # agent = A2C.load("a2c_doapp", env=env, print_system_info=True)
        print("Loaded")
        agent = A2C.load("a2c_sfiii3n", env=env, print_system_info=True)
    except:
        print("Made new")
        # Save the agent
        agent.save("a2c_sfiii3n")
        # Load the agent
        agent = A2C.load("a2c_sfiii3n", env=env, print_system_info=True)
    
    return agent

def save_agent(agent):
    agent.save("a2c_sfiii3n")

def load_cumulative_rewards():
    cumulative_rewards = []
    if os.path.exists('cumulative_rewards.json'):
        with open('cumulative_rewards.json', 'r') as json_file:
            cumulative_rewards = json.load(json_file)
    return cumulative_rewards

def save_cumulative_rewards(cumulative_rewards):
    with open('cumulative_rewards.json', 'w') as json_file:
        json.dump(cumulative_rewards, json_file)

def main():
    cumulative_rewards = load_cumulative_rewards()

    # Continue training or start from scratch
    existing_iterations = len(cumulative_rewards)

    # Settings start here
    settings = {}

    # Player side selection: P1 (left), P2 (right), Random (50% P1, 50% P2)
    settings["player"] = "P1"

    # Number of steps performed by the game
    # for every environment step, bounds: [1, 6]
    settings["step_ratio"] = 6

    # Native frame resize operation
    # settings["frame_shape"] = (480, 480, 0)  # RBG with 128x128 size
    # settings["frame_shape"] = (0, 0, 1) # Grayscale with original size
    settings["frame_shape"] = (0, 0, 0) # Deactivated (Original size RBG)

    # Game continue logic (0.0 by default):
    # - [0.0, 1.0]: probability of continuing game at game over
    # - int((-inf, -1.0]): number of continues at game over
    #                      before episode to be considered done
    settings["continue_game"] = 0.0

    # If to show game final when game is completed
    settings["show_final"] = True

    # If to use hardcore mode in which observations are only made of game frame
    settings["hardcore"] = True

    # Game-specific options (see documentation for details)
    # Game difficulty level
    settings["difficulty"] = 4

    # Character to be used, automatically extended with "Random" for games
    # required to select more than one character (e.g. Tekken Tag Tournament)
    settings["characters"] = "Q"

    # If to use discrete or multi_discrete action space
    settings["action_space"] = "multi_discrete"

    # If to use attack buttons combinations actions
    settings["attack_but_combination"] = True

    # Settings end here

    env = diambra.arena.make("sfiii3n", settings)

    # env, num_envs = make_sb3_env("sfiii3n", settings)

    # Instantiate the agent
    agent = A2C("CnnPolicy", env)
    
    prep(agent, env)

    agent.set_env(env)

    # Train the agent
    agent.learn(total_timesteps=30000, progress_bar=True)

    save_agent(agent)

    # Evaluate the agent
    # NOTE: If you use wrappers with your environment that modify rewards,
    #       this will be reflected here. To evaluate with original rewards,
    #       wrap environment in a "Monitor" wrapper before other wrappers.
    mean_reward, std_reward = evaluate_policy(model=agent, env=agent.get_env(), n_eval_episodes=3)
    print("Reward: {} (avg) ± {} (std)".format(mean_reward, std_reward))

    # Run trained agent
    observation = env.reset()
    cumulative_reward = 0
    # env.show_obs(observation)

    while True:
        env.render()

        action, _state = agent.predict(observation, deterministic=True)

        actions = env.action_space.sample()
        print("Actions: {}".format(actions))

        observation, reward, done, info = env.step(actions)
        # env.show_obs(observation)
        cumulative_reward += reward

        print("Reward: {}".format(reward))
        print("Done: {}".format(done))
        print("Info: {}".format(info))
        if (reward != 0):
            print("Cumulative reward =", cumulative_reward)

        if done:
            observation = env.reset()
            # env.show_obs(observation)
            current_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            cumulative_rewards.append({'date': current_date, 'cumulative_reward': cumulative_reward})
            save_cumulative_rewards(cumulative_rewards)
            break

    env.close()

    return 0

if __name__ == '__main__':
    main()