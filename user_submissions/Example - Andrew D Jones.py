from Util import Action, PAYOFF, ROUNDS
from Player import Player

'''
Action enum for valid moves:
    Action.CHEAT
    Action.COOPERATE

You can access the payoff matrix with PAYOFF
You can access the number of rounds between two people with ROUNDS

'''

from enum import Enum

class Action(Enum):
    CHEAT = 0
    COOPERATE = 1

PAYOFF = [[0, 3],
          [-1, 2]]

REPRODUCE = 15 #
ROUNDS = 10
GAMES = 50
NOISE = 0.05

class Example(Player):
    def initialize(self) -> None:
        self.cooperate_count = 0
        self.cheat_count = 0

    def act(self) -> Action:
        # Adaptive Strategy:
        # Initially, cooperate. If the opponent cheats more than cooperates, start cheating.
        if len(self.other_history) == 0:
            return Action.COOPERATE  # Cooperate first time

        # Count the number of times the opponent cooperated and cheated
        cooperate_count = sum(1 for action in self.other_history if action == Action.COOPERATE)
        cheat_count = sum(1 for action in self.other_history if action == Action.CHEAT)

        # Adjust the strategy based on the opponent's behavior
        if cheat_count > cooperate_count:
            self.cheat_count += 1
            return Action.CHEAT
        else:
            self.cooperate_count += 1
            return Action.COOPERATE

    def update(self) -> None:
        # You can update any state variables or perform actions after each round here.
        pass

