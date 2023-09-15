from Player import Player
from Util import *

class SpitefulTFT (Player):
    def __init__(self):
        super().__init__()
        spiteful = False

    def act(self):
        if spiteful:
            return Action.CHEAT

        if len(other_history) == 0:
            return Action.COOPERATE

        if other_history[-1] <= 0:
            if len(other_history) >= 2 and other_history[-2] <= 0:
                spiteful = True
            return Action.CHEAT
        return Action.COOPERATE

    def reset():
        super.reset()
        spiteful = False
