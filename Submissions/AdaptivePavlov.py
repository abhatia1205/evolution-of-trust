from Player import Player
from Util import *

class AdaptivePavlov(Player):

    def __init__(self):
        self.score = 0
        self.other_history = []
        self.self_history = []
        self.other_class = "Cooperative"
    
    def _act(self):
        #Tit for Tat for first 6 rounds
        if len(self.self_history) <= 6:
            return Action.COOPERATE if self.other_history[-1] == Action.COOPERATE else Action.CHEAT
        if len(self.self_history) % 6 == 0:
            # Classify opponent
            if self.other_history[-6:] == [Action.COOPERATE] * 6:
                self.other_class = "Cooperative"
            if self.other_history[-6:].count(Action.CHEAT) >= 4:
                self.other_class = "ALLD"
            if self.other_history[-6:].count(Action.CHEAT) == 3:
                self.other_class = "STFT"
            if not self.other_class:
                self.opponent_class = "Random"
        if self.opponent_class in ["Random", "ALLD"]:
            return Action.CHEAT
        if self.opponent_class == "STFT":
            # TFTT
            return Action.CHEAT if self.other_history[-2:] == [Action.CHEAT, Action.CHEAT] else Action.COOPERATE
        if self.opponent_class == "Cooperative":
            # TFT
            return Action.CHEAT if self.other_history[-1:] == [Action.CHEAT] else Action.COOPERATE
        pass
