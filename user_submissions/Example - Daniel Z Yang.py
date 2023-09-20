from Player import Player
from Util import Action

class Example(Player):
    def initialize(self) -> None:
        self.round_count = 0
        self.tit_for_tat_rounds = 7
        self.cheat = False

    def act(self) -> Action:
        if self.round_count < self.tit_for_tat_rounds:
            if self.round_count == 0:
                return Action.COOPERATE  # Cooperate in the first round
            elif len(self.other_history) > 0:
                return self.other_history[-1]  # Copy opponent's last move
            else:
                return Action.COOPERATE  # Default to cooperate if no history is available
        else:
            if len(self.other_history) > 0:
                opponent_cheat_count = self.other_history.count(Action.CHEAT)
                if opponent_cheat_count / len(self.other_history) > 0.5:
                    self.cheat = True
                else:
                    self.cheat = False

            if self.cheat:
                return Action.CHEAT  # Switch to grudge if over 50% of opponent's history is cheating
            elif len(self.other_history) > 0:
                return self.other_history[-1]  # Continue copying opponent's last move
            else:
                return Action.COOPERATE  # Default to cooperate if no history is available

    def update(self) -> None:
        self.round_count += 1
