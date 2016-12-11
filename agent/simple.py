# -*- coding: utf-8 -*-

from agent.agent import Agent

class SimpleAgent(Agent):

    def __init__(self, enable_action):

        super().__init__(enable_action)
        self.action_time = 0
 
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
        
        """同じ動作を連続させてみるOpenAIの場合元々、以下の処理で１回で複数の動作が行われるが
        さらにaction 0 : "NOOP" を置くことで前の処理を連続させてみる
        self.frameskip = (2, 5)
        
        if isinstance(self.frameskip, int):
            num_steps = self.frameskip
        else:
            num_steps = self.np_random.randint(self.frameskip[0], self.frameskip[1])
        for _ in range(num_steps):
            reward += self.ale.act(action)
        """
        
        action = 0
        if self.action_time % 4 == 0:        
            if len(best_action_list) > action_step  \
            and self.__action_reward(best_action_list, action_step) > 0:
                action = best_action_list[action_step][0]
            else:
                action = self._random_action()
                
        self.action_time = self.action_time + 1
         
        return action

  

            
    

