from Player import Player
from Util import *

class SpitefulTFT (Player):
    def __init__(self):
        super().__init__()
        self.spiteful = False

    def act(self):
        if self.spiteful:
            return Action.CHEAT

        if len(self.other_history) == 0:
            return Action.COOPERATE

        if self.other_history[-1] <= 0:
            if len(self.other_history) >= 2 and self.other_history[-2] <= 0:
                self.spiteful = True
            return Action.CHEAT
        return Action.COOPERATE

    def reset(self):
        self.spiteful = False
