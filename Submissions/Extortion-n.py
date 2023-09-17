#Extortion-n Method 
from Util import *
from Player import *
import random
class Extort2Player(Player):

    def initialize(self):
        pass

    def act(self):
        if not self.self_history:
            return Action.COOPERATE

        last_pair = (self.self_history[-1], self.other_history[-1])

        prob = 0

        if last_pair == (Action.COOPERATE, Action.COOPERATE):
            prob = 7/8
        elif last_pair == (Action.COOPERATE, Action.CHEAT):
            prob = 7/16
        elif last_pair == (Action.CHEAT, Action.COOPERATE):
            prob = 3/8
        else:
            prob = 0

        return Action.COOPERATE if random.random() < prob else Action.CHEAT

    def update(self):
        pass

    def reset(self):
        pass