from Util import *

class Player():

    def __init__(self):
        self.score = 0
        self.history = []
    
    def reset(self):
        self.history = []

    def _update(self, other_action: Action, score: int):
        self.history.append(other_action)
        self.score += score 

    def _reset(self):
        self.reset()
        self.history = []
    
    def _act(self):
        pass
