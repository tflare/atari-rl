# -*- coding: utf-8 -*-

import random

class Agent:

    def __init__(self, enable_action):

        self.enable_action = enable_action
        self.action_time = 0
        
    def __random_action(self):
    
        return(random.choice(self.enable_action))
 
    def __action_reward(self, best_action_list, action_step):
        
        # ToDo Q-Learning ADD

        reward = 0
        diff_max = 5

        if len(best_action_list) > (action_step + diff_max):
            for diff in range(0, diff_max):         
                reward = reward + best_action_list[action_step + diff][1]
                       
        return reward


    def action_select(self, action_step, best_action_list):
        
        # ToDo ϵ-greedy法 ADD
        
        # アクション時の獲得rewardが0を超えるなら、ベストスコア時のアクションを実施する。
         # それ以外はランダムな動きをする。
        

        action = 0
        if self.action_time % 4 == 0:        
            if len(best_action_list) > action_step  \
            and self.__action_reward(best_action_list, action_step) > 0:
                action = best_action_list[action_step][0]
            else:
                action = self.__random_action()
                
        self.action_time = self.action_time + 1
         
        return action

  

            
    

