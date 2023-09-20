from Player import Player
from Util import *

class TFT (Player):
    def __init__(self):
        super().__init__()

    def act(self):
        return Action.CHEAT