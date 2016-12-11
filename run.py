# -*- coding: utf-8 -*-

import main
from agent.simple import SimpleAgent
from agent.random import RandomAgent

"""
ACTION_MEANING = {
    0 : "NOOP",
    2 : "UP",
    3 : "RIGHT",
    4 : "LEFT",
    5 : "DOWN",
}
"""

enable_action = [0, 2, 3, 4, 5]

#agent = SimpleAgent(enable_action)
agent = RandomAgent(enable_action)
render = True
main.atari_start('MsPacman-v0', agent, render)
