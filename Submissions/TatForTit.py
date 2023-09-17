#Tat-for-tit
#Opposite of Tit for Tat, does the opposite of what tit-for-tat would do, but starts out cooperating
from Util import *
from Player import *

class TatforTit(Player):

    def act(self) -> Action:
 
        return Action.CHEAT if self.other_history[-1:] == [Action.COOPERATE] else Action.COOPERATE