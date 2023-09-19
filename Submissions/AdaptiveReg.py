
from Player import Player
from Util import *


class Adaptive(Player):
    """Start with a specific sequence of C and D, then play the strategy that
    has worked best, recalculated each turn.

    """

    name = "Adaptive"


    def __init__(self):
        super().__init__()
        initial_plays = [Action.COOPERATE] * 6 + [Action.CHEAT] * 5
        self.initial_plays = initial_plays
        self.scores = {Action.COOPERATE: 0, Action.CHEAT: 0}

    def score_last_round(self, opponent: Player):
        # Load the default game if not supplied by a tournament.
        if len(self.self_history):
            last_round = (self.self_history[-1], opponent.self_history[-1])
            scores = self.score(last_round) #changed from self.game to self.score?
            self.scores[last_round[0]] += scores[0]

    def act(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        # Update scores from the last play
        self.score_last_round(opponent)
        # Begin by playing the sequence C,C,C,C,C,C,D,D,D,D,D
        index = len(self.history)
        if index < len(self.initial_plays):
            return self.initial_plays[index]
        # Play the strategy with the highest average score so far
        if self.scores[Action.COOPERATE] > self.scores[Action.CHEAT]:
            return Action.COOPERATE
        return Action.CHEAT