from Player import Player
from Util import *
import random

class Copycat(Player):
    def __init__(self):
        super().__init__()
    
    def act(self):
        return self.other_history[-1] if len(self.other_history) == 0 else Action.COOPERATE

class AlwaysCheat(Player):
    def __init__(self):
        super().__init__()
    
    def act(self):
        return Action.CHEAT
    
class Random(Player):
    def __init__(self):
        super().__init__()
    
    def act(self):
        return random.choice(Action)
    
class Grudge(Player):
    def __init__(self):
        super().__init__()
    
    def act(self):
        if self.other_history and list(map(lambda x: True if x == Action.CHEAT else False, 
                                           self.other_history)).any():
            return Action.CHEAT
        else:
            return Action.COOPERATE

class Detective(Player):
    def initialize(self):
        self.begin_choices = [Action.COOPERATE, Action.CHEAT, Action.COOPERATE, Action.COOPERATE]
        self.copycat_mode = False
    
    def act(self):
        if len(self.self_history) < 4:
            return self.begin_choices[len(self.self_history)]
        elif self.copycat_mode:
            return self.other_history[-1]
        else:
            return Action.CHEAT
        
    def update(self):
        if self.other_history[-1] == Action.CHEAT:
            self.copycat_mode = True

class Copykitten(Player):
    def __init__(self):
        super().__init__()
    
    def act(self):
        if len(self.other_history) < 2 or not (self.other_history[-1] == Action.CHEAT and 
                                               self.other_history[-2] == Action.CHEAT):
            return Action.COOPERATE
        else:
            return Action.CHEAT
        
class Simpleton(Player):
    def __init__(self):
        super().__init__()
    
    def act(self):
        if not self.other_history:
            return Action.COOPERATE
        elif self.other_history[-1] == Action.COOPERATE:
            return self.self_history[-1]
        else:
            return Action.CHEAT if self.self_history[-1] == Action.COOPERATE else Action.COOPERATE
