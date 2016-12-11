# -*- coding: utf-8 -*-

import random

class Agent(object):

    def __init__(self, enable_action):

        self.enable_action = enable_action

    def __action_reward(self):
        return 0

    def random_action(self):
        return(random.choice(self.enable_action))

    def action_select(self):
        # 0 is noop
        return 0
