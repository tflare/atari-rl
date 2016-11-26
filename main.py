# -*- coding: utf-8 -*-

import gym
import json

from agent_action import AgentAction


def print_avarage_result(episode_times, time, total_reward):
    print("avarage {} steps".format((time+1) / episode_times))
    print("avarage_reward was {}".format(total_reward / episode_times)) 


def print_result(episode_times, time, total_reward):
    print("Episode {}:".format(episode_times))
    print(" {} steps".format((time+1)))
    print("reward was {}".format(total_reward)) 


def debug_action_output(action_list, episode):
    with open("actionlist{}.txt".format(episode), 'w') as file:
        for inner_list in action_list:
            json.dump(inner_list, file)


def pacman_start():
    atari_start('MsPacman-v0')


def atari_start(game_name):
    
    atari_env = gym.make(game_name)
    
    all_time = 0
    all_reward = 0
    episode_times = 20
    best_total_reward = 0
    best_action_list = []
    
    for episode in range(episode_times):
        atari_env.reset()
        
        #
        for _ in range(200):
            atari_env.step(0)
              
        total_reward = 0
        action_step = 0        
        action_list = []

        for time in range(2000):
            atari_env.render()
            
            aaction = AgentAction()
            action = aaction.action_select(action_step, best_action_list)
            action_step = action_step + 1
           
            observation, reward, done, info = atari_env.step(action)
            lives = float(atari_env.ale.lives())
            
            action_list.append([action, reward, lives])
            total_reward = total_reward + reward
            if done:
                print_result(episode, time, total_reward)
                
                all_time = all_time + time
                all_reward = all_reward + total_reward
                
                if best_total_reward < total_reward:
                    best_total_reward = total_reward
                    best_action_list = action_list
                    
                debug_action_output(action_list, episode)
                
                break
                
    print_avarage_result(episode_times, all_time, all_reward)
    atari_env.monitor.close()
    


