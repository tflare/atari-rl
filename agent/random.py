# -*- coding: utf-8 -*-

from agent.agent import Agent


class RandomAgent(Agent):

    def action_select(self, action_step, best_action_list):
        return super()._random_action()
