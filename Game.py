from typing import Dict, Type 
from Player import Player
from Util import Action
from collections import defaultdict
import numpy as np
import copy

class Game():

    def __init__(self):
        self.players = []
        self.noise = 0
        self.payoff = np.array([[0, 3],
                       [-1, 2]])
        self.reproduce = 5
        self.rounds = 7
    
    def __init__(self, player_dict: Dict[Type, int]):
        for key, val in player_dict:
            [self.players.append(key()) for i in range(val)]
    
    def print_players(self):
        d = defaultdict()
        for player in self.players():
            d[type(player).__name__] += 1
        for key, val in sorted(d.items(), lambda kv: kv[1]):
            print(f"{key}: {val}", end = " ")
        print("\n")
    
    def reproduce(self):
        l = sorted(self.players, key = lambda x: x.score())[:-self.reproduce]
        for i in range(self.reproduce):
            l.append(copy.deepcopy(l[i]))
        self.players = l
        

    def round(self):
        for i in range(len(self.players)):
            for j in range(i+1, len(self.players)):
                for k in range(self.round):
                    p1 = self.players[i].act()
                    p2 = self.players[j].act()
                    self.players[i]._update(p1, p2, self.payoff[(p1, p2)])
                    self.players[j]._update(p2, p1, self.payoff[(p2, p1)])
                self.players[i]._reset()
                self.players[j]._reset()
        self.reproduce()
        self.print_players()

    def tournament(self):
        pass

    