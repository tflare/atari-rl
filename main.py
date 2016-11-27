# -*- coding: utf-8 -*-

import gym
import os
import csv

from action_agent import ActionAgent


def print_avarage_result(episode_times, step, total_reward):
    print("avarage {} steps".format((step+1) / episode_times))
    print("avarage_reward was {}".format(total_reward / episode_times)) 


def print_result(episode_times, step, total_reward):
    print("Episode {}:".format(episode_times))
    print(" {} steps".format((step+1)))
    print("reward was {}".format(total_reward)) 


def debug_action_output(action_list, episode):

    script_dir = os.path.abspath(os.path.dirname(__file__))
    debug_dir  = os.path.join(script_dir, 'debug')
    if(os.path.isdir(debug_dir) == False):
        os.mkdir(debug_dir)    
    
    debug_file_path =os.path.join(debug_dir, "actionlist{}.csv".format(episode))
    
    with open(debug_file_path, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(action_list)





def atari_start(game_name, enable_action):
    
    atari_env = gym.make(game_name)
    
    all_step = 0
    all_reward = 0
    episode_times = 20
    best_total_reward = 0
    best_action_list = []
    
    for episode in range(episode_times):
        
        observation = atari_env.reset()
  
        total_reward = 0
        action_step = 0        
        action_list = []
        act_agent = ActionAgent(enable_action)
        done = False

        no_op_steps = 100
        for before_step in range(no_op_steps):
            observation, _, _, _ = atari_env.step(0)
            #if(no_op_steps - 1 == no_op_steps -1):
                #last_observation = observation

        #state = act_agent.get_initial_state(observation, last_observation)
            
        while not done:
            #last_observation = observation
            action = act_agent.action_select(action_step, best_action_list)                
            
            action_step = action_step + 1
           
            observation, reward, done, info = atari_env.step(action)
            atari_env.render()
            
            #lives = float(atari_env.ale.lives())
            
            action_list.append([action, reward])
            total_reward = total_reward + reward
            if done:
                print_result(episode, action_step, total_reward)
                
                all_step = all_step + action_step
                all_reward = all_reward + total_reward
                
                if best_total_reward < total_reward:
                    best_total_reward = total_reward
                    best_action_list = action_list
                    
                    print(best_total_reward)
                    
                debug_action_output(action_list, episode)
                
                break
                
    print_avarage_result(episode_times, all_step, all_reward)
    atari_env.monitor.close()
    


