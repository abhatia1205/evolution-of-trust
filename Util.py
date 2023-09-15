from enum import Enum

class Action(Enum):
    CHEAT = 0
    COOPERATE = 1

PAYOFF = [[0, 3],
          [-1, 2]]
REPRODUCE = 5
ROUNDS = 7
GAMES = 20