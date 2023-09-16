
from Player import Player
from Util import *
import numpy as np


class TwoTitForTatDynamic(Player):
    """
    A player starts by cooperating and then punishes its opponent's
    defections with defections, but with a dynamic bias towards cooperating
    based on the opponent's ratio of cooperations to total moves
    (so their current probability of cooperating regardless of the
    opponent's move (aka: forgiveness)).

    """


    def act(self):
        # strategy definition that determines player's action
        # First move
        if not self.other_history:
            # Make sure we cooperate first turn
            return Action.COOPERATE
        if Action.CHEAT in self.other_history[-2:]:
            # Probability of cooperating regardless
            return np.random.random_choice( #random choice
                self.other_history.count(Action.COOPERATE) / len(self.other_history)
            )
        else:
            return Action.COOPERATE