from Util import *

class Player():

    def __init__(self):
        self.score = 0
        self.other_history = []
        self.self_history = []
    
    def reset(self):
        pass

    def _update(self, self_action: Action, other_action: Action, score: int):
        self.other_history.append(other_action)
        self.self_history.append(self_action)
        self.score += score 

    def _reset(self):
        self.reset()
        self.other_history = []
        self.self_history = []
    
    def act(self):
        pass