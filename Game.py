from typing import Dict, Type, List
from Player import Player
from Util import Action
from collections import defaultdict
from Submissions.AdaptivePavlov import AdaptivePavlov
from Submissions.nPavlov import nPavlov
import numpy as np
import copy

class Game():

    def __init__(self):
        self.players: List[Player] = []
        self.noise = 0
        self.payoff = np.array([[0, 3],
                       [-1, 2]])
        self.REPRODUCE = 5
        self.ROUNDS = 7
        self.GAMES = 20
    
    def __init__(self, player_dict: Dict[Type, int]):
        for key, val in player_dict:
            [self.players.append(key()) for i in range(val)]
    
    def print_players(self):
        d = defaultdict()
        for player in self.players():
            d[type(player).__name__] += 1
        for key, val in sorted(d.items(), lambda kv: kv[1]):
            print(f"\t{key}: {val}", end = "\n")
        print("\n")
    
    def reproduce(self):
        l = sorted(self.players, key = lambda x: x.score())[:-self.reproduce]
        for i in range(self.REPRODUCE):
            l.append(copy.deepcopy(l[i]))
        self.players = l
        

    def standoff(self, player1: Player, player2: Player):
        for k in range(self.ROUNDS):
            p1 = player1.act()
            p2 = player2.act()
            player1._update(p1, p2, self.payoff[(p1, p2)])
            player2._update(p2, p1, self.payoff[(p2, p1)])
        player1._reset()
        player2._reset()

    def round(self):
        #set up players lol
        for i in range(len(self.players)):
            for j in range(i+1, len(self.players)):
                self.standoff()
    
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
    dict = {AdaptivePavlov: 15, nPavlov: 15}
    g = Game(dict)
    g.game()
main()

    