from enum import Enum

class Action(Enum):
    CHEAT = 0
    COOPERATE = 1

PAYOFF = [[0, 3],
          [-1, 2]]

REPRODUCE = 15 #
ROUNDS = 10
GAMES = 2000
NOISE = 0
NUM_INITIAL_PLAYERS = 5