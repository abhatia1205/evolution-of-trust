from typing import Dict, Type, List
from Player import Player
from Util import *
from collections import defaultdict
from Submissions.AdaptivePavlov import AdaptivePavlov
from Submissions.nPavlov import nPavlov
import numpy as np
import copy
from Submissions.GradualPlayer import Gradual

class Game():

    def __init__(self, player_dict: Dict[Type, int]):
        self.players: List[Player] = []
        self.noise = 0
        self.payoff = [[0, 3],
                       [-1, 2]]
        self.REPRODUCE = 5
        self.ROUNDS = 7
        self.GAMES = 20

        for key, val in player_dict.items():
            [self.players.append(key()) for i in range(val)]
        
    def print_players(self):
        d = defaultdict(lambda: 0)
        for player in self.players:
            d[type(player).__name__] = d[type(player).__name__] + 1
        for key, val in sorted(d.items(), key = lambda kv: kv[1]):
            print(f"\t{key}: {val}", end = "\n")
        print("\n")
    
    def reproduce(self):
        l = sorted(self.players, key = lambda x: x._get_score())
        l = l[:-self.REPRODUCE]
        for i in range(self.REPRODUCE):
            l.append(copy.deepcopy(l[i]))
        self.players = l
        

    def standoff(self, player1: Player, player2: Player):
        for k in range(self.ROUNDS):
            p1 = player1.act()
            p2 = player2.act()
            assert isinstance(p1, Action)
            assert isinstance(p1, Action)
            p1, p2 = p1.value, p2.value
            player1._update(p1, p2, self.payoff[p1][p2])
            player2._update(p2, p1, self.payoff[p2][p1])
        player1._reset()
        player2._reset()

    def round(self):
        #set up players lol
        for i in range(len(self.players)):
            for j in range(i+1, len(self.players)):
                self.standoff(self.players[i], self.players[j])
    
    def game(self):
        print("Starting game")
        for i in range(self.GAMES):
            print('Starting state: \n')
            self.print_players()

            self.round()
            self.reproduce()
            
            print('End state after reproduction: \n')
            self.print_players()
            print("\n")

def main():
    dict = {AdaptivePavlov: 15, nPavlov: 15, Gradual: 15}
    g = Game(dict)
    g.game()
main()

    