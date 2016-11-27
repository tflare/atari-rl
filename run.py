# -*- coding: utf-8 -*-

import main

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

main.atari_start('MsPacman-v0', enable_action)
