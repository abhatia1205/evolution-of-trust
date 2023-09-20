from Player import Player
from Util import *

class always_cooperate (Player):
    def __init__(self):
        super().__init__()

    def act(self):
        return Action.COOPERATE