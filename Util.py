from enum import Enum

class Action(Enum):
    CHEAT = 0
    COOPERATE = 1

PAYOFF = [[0, 3],
          [-1, 2]]

REPRODUCE = 15 #
ROUNDS = 100
GAMES = 17