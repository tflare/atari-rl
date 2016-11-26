# -*- coding: utf-8 -*-

import random

class AgentAction:
   
    def __random_action(self):
    
        """
        ACTION_MEANING = {
            0 : "NOOP",
            2 : "UP",
            3 : "RIGHT",
            4 : "LEFT",
            5 : "DOWN",
        }
        """

        return random.choice([0, 2, 3, 4, 5])
    
    
    def __action_reward(self, best_action_list, action_step):
        
        # ToDo Q-Learning ADD

        reward = 0
        diff_max = 5

        if len(best_action_list) > (action_step + diff_max):
            for diff in range(0, diff_max):         
                reward = reward + best_action_list[action_step + diff][1]
                       
        return reward

    def __reverse_action(self, action):
        if(action == 2):
            return 5
        elif(action == 3):
            return 4
        elif(action == 4):
            return 3           
        elif(action == 5):            
            return 2           
        
    def __lives_lost_reverse(self, action_step, best_action_list):
        
        if len(best_action_list) > action_step:
            before_lives = best_action_list[action_step-1][2]
            lives = best_action_list[action_step][2]
    
            if(before_lives > lives):
                best_action_list[action_step][0] = self.__reverse_action(best_action_list[action_step][0])             
            
        return best_action_list
  
        
    def action_select(self, action_step, best_action_list):
        
        # ToDo ϵ-greedy法 ADD
        
        # アクション時の獲得rewardが0を超えるなら、ベストスコア時のアクションを実施する。
         # それ以外はランダムな動きをする。
        

        action = 0
        
        if len(best_action_list) > action_step  \
        and self.__action_reward(best_action_list, action_step) > 0:
            action = best_action_list[action_step][0]
        else:
            action = self.__random_action()
     
    
        return action
            
    

