from Util import *

class Player():

    def initialize(self):
        pass

    def __init__(self):
        self._score = 0
        self.other_history = []
        self.self_history = []
        self.initialize()
    
    def act(self):
        pass

    def update(self):
        pass

    def reset(self):
        pass

    def _update(self, self_action: Action, other_action: Action, score: int):
        self.other_history.append(other_action)
        self.self_history.append(self_action)
        self._score += score
        self.update()

    def _reset(self):
        self.initialize()
        self.reset()
        self._clear_history()

    def _get_score(self):
        return self._score
    
    def _act(self):
        try:
            action = self.act()
            if isinstance(action, Action):
                return action
            else:
                return Action.COOPERATE
        except:
            return Action.COOPERATE

    def _clear_history(self):
        self.other_history = []
        self.self_history = []
