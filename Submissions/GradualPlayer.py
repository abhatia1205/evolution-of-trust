#Gradual Player
from Util import *
from Player import *

class Gradual(Player):
    def initialize(self) -> None:
        self.calm_count = 0
        self.punish_count = 0

    def act(self) -> Action:

        if len(self.other_history) == 0:
            return Action.COOPERATE

        if self.punish_count > 0:
            self.punish_count -= 1
            return Action.CHEAT

        if self.calm_count > 0:
            self.calm_count -= 1
            return Action.COOPERATE

        if self.other_history[-1] == Action.CHEAT:
            self.punish_count = self.other_history.count(Action.CHEAT)
            self.calm_count = 2
            return Action.CHEAT
        return Action.COOPERATE