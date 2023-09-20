from typing import Dict, Type, List
from Player import Player
from Util import *
from collections import defaultdict
from Submissions.AdaptivePavlov import AdaptivePavlov
from Submissions.AdaptiveReg import Adaptive
from Submissions.nPavlov import nPavlov
from Submissions.TwoTitForTatDynamic import TwoTitForTatDynamic
from Submissions.SpitefulTFT import SpitefulTFT
from Submissions.GradualPlayer import Gradual
from Submissions.SuspiciousTFTPlayer import SuspiciousTitForTat
from Submissions.Basics import *
from Submissions.TFT import TFT
import numpy as np
import copy
from random import random

class Game():

    def __init__(self, player_dict: Dict[Type, int]):
        self.players: List[Player] = []
        self.noise = NOISE
        self.payoff = [[0, 3],
                       [-1, 2]]
        self.REPRODUCE = REPRODUCE
        self.ROUNDS = ROUNDS
        self.GAMES = GAMES
        self.removed = set()

        for key, val in player_dict.items():
            [self.players.append(key()) for i in range(val)]
        
    def print_players(self):
        d = defaultdict(lambda: 0)
        for player in self.players:
            d[type(player).__name__+type(player).__module__] = d[type(player).__name__+type(player).__module__] + 1
        for key, val in sorted(d.items(), key = lambda kv: kv[1]):
            print(f"\t{key}: {val}", end = "\n")
        print('Removed: ', self.removed)
        print("\n")
    
    def reproduce(self):
        self.removed = set()
        l = sorted(self.players, key = lambda x: -x._get_score())
        for i in l[-REPRODUCE:]:
            self.removed.add(type(i))
        l = l[:-REPRODUCE]
        for i in range(REPRODUCE):
            l.insert(0, copy.deepcopy(l[i + i]))
        self.players = l

    def standoff(self, player1: Player, player2: Player):
        for k in range(ROUNDS):
            p1 = player1._act()
            p2 = player2._act()
            assert isinstance(p1, Action)
            assert isinstance(p1, Action)
            p1 = Action(1 - p1.value) if random() < self.noise else p1
            p2 = Action(1 - p2.value) if random() < self.noise else p2
            player1._update(p1, p2, self.payoff[p1.value][p2.value])
            player2._update(p2, p1, self.payoff[p2.value][p1.value])
        player1._clear_history()
        player2._clear_history()

    def round(self):
        #set up players lol
        for i in range(len(self.players)):
            for j in range(i+1, len(self.players)):
                self.standoff(self.players[i], self.players[j])
    
    def game(self):
        print("Starting game")
        for i in range(GAMES):
            # print('Starting state: \n')
            # self.print_players()
            np.random.shuffle(self.players)
            self.round()
            self.reproduce()
            for player in self.players:
                player._reset()
                player._score=0
            
            print('End state after reproduction: \n')
            self.print_players()


def main():
    dict = {Copycat:15, AlwaysCheat: 15, Random: 15, Grudge: 15, Copykitten: 15, Simpleton: 15,
            Gradual: 15, SpitefulTFT: 15, SuspiciousTitForTat: 15, AdaptivePavlov: 15, 
            TFT: 15}
    g = Game(dict)
    g.print_players()
    g.game()

if __name__ == '__main__':
    main()

