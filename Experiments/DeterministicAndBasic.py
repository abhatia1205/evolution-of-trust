import sys
sys.path.append('../')
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
from Submissions.TatForTit import TatforTit
# import numpy as np
import Game as Game
import copy



def main():
    #all
    d = {Copycat: 15, AlwaysCheat: 15, Grudge: 15, Copykitten: 15, Simpleton: 15,
            Gradual: 15, SpitefulTFT: 15, SuspiciousTitForTat: 15, AdaptivePavlov: 15, 
          TatforTit: 15}
#     #minus suspicious tit for tat
#     d = {Copycat: 15, AlwaysCheat: 15, Random: 15, Grudge: 15, Copykitten: 15, Simpleton: 15,
#             Gradual: 15, SpitefulTFT: 15, AdaptivePavlov: 15, 
#             TFT: 15, TatforTit: 15}
#     #minus copycat
#     d = {AlwaysCheat: 15, Random: 15, Grudge: 15, Copykitten: 15, Simpleton: 15,
#             Gradual: 15, SpitefulTFT: 15, AdaptivePavlov: 15, 
#             TFT: 15, TatforTit: 15}
#     #minus rand, grudge, spiteful
#     d = {AlwaysCheat: 15, Copykitten: 15, Simpleton: 15,
#             Gradual: 15, AdaptivePavlov: 15, 
#             TFT: 15, TatforTit: 15}
    
#     d = {AlwaysCheat: 15, Copykitten: 15,
#             Gradual: 15, AdaptivePavlov: 15, 
#             TFT: 15, TatforTit: 15}
    
#     d = {AlwaysCheat: 15, Copykitten: 15,
#             Gradual: 15, AdaptivePavlov: 15, 
#             TFT: 15}
    
    g = Game.Game(d)
    g.print_players()
    g.game()

    
#     matrix = [[0 for i in range(5)] for j in range(6)]

#     for noise in [0,0.02, 0.05, 0.1, 0.2, 0.4]:
#         for num_rounds in [10, 20, 50, 100, 200]:
#                 g = Game.Game(d)
#                 g.ROUNDS = num_rounds
#                 g.noise = noise
#                 g.print_players()
#                 g.game()

    
#     d = { Copykitten: 15,
#             Gradual: 15, AdaptivePavlov: 15, 
#             TFT: 15, SuspiciousTitForTat: 15}


if __name__ == '__main__':
    main()

'''
params: 
REPRODUCE = 15
ROUNDS = 10
GAMES = 17

SuspiciousTFT

CopyCat

Grudge, SpitefulTFT, Random

Simpleton

Tat for Tit

Always Cheat

Gradual, Adaptive Pavlov, CopyKitten
'''