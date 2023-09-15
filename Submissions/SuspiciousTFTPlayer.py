#Suspicious TFT Player
from Util import *
from Player import *

class SuspiciousTitForTat(Player):

    def act(self) -> Action:
 
        return Action.COOPERATE if self.other_history[-1:] == [Action.COOPERATE] else Action.CHEAT