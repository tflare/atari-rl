# -*- coding: utf-8 -*-

import gym
import os
import csv


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


def atari_start(game_name, agent, render = True):
    
    gym_env = gym.make(game_name)
    gym_env.monitor.start('/tmp/' + game_name, force=True)
    
    all_step = 0
    all_reward = 0
    episode_times = 5
    best_total_reward = 0
    best_action_list = []
    
    for episode in range(episode_times):
        
        observation = gym_env.reset()
  
        total_reward = 0
        action_step = 0        
        action_list = []
        done = False

        #初期化　何故かこれぐらいやらないとうまくいかない。
        #自分のバグ？
        ep_frame_number = 0
        while ep_frame_number < 258:
            observation, _, _, _ = gym_env.step(0)
            ep_frame_number = float(gym_env.ale.getEpisodeFrameNumber())
            #gym_env.render()
            
        while not done:

            action = agent.action_select(action_step, best_action_list)                
            
            action_step = action_step + 1
           
            observation, reward, done, info = gym_env.step(action)
            
            if render:
                gym_env.render()
            
            #lives = float(atari_env.ale.lives())
            ep_frame_number = float(gym_env.ale.getEpisodeFrameNumber())
            
            action_list.append([action, reward, ep_frame_number])
            total_reward = total_reward + reward


        print_result(episode, action_step, total_reward)
        
        all_step = all_step + action_step
        all_reward = all_reward + total_reward
        
        if best_total_reward < total_reward:
            best_total_reward = total_reward
            best_action_list = action_list
            
            print(best_total_reward)
            
        debug_action_output(action_list, episode)
                
    print_avarage_result(episode_times, all_step, all_reward)
    gym_env.monitor.close()
    
