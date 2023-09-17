from Player import Player
from Util import *

class TFT (Player):
    def __init__(self):
        super().__init__()

    def act(self):
        if len(self.other_history) == 0:
            return Action.COOPERATE

        return self.other_history[-1]
