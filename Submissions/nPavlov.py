import numpy as np
from Player import Player
from Util import *

class nPavlov(Player):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.other_history = []
        self.self_history = []
        self.pCoop = 1
        self.currRound = 0;
    
    def reset(self):
        self.reset()
        self.other_history = []
        self.self_history = []
        self.pCoop = 1
        self.currRound = 0
    
    def act(self):
        #Tit for Tat for first 6 rounds
        if(self.currRound == 0):
            self.currRound += 1
            return Action.COOPERATE
        myLastMove = self.self_history[-1]
        enemyLastMove = self.other_history[-1]
        #if payoff (enemy is cooperating and I am cooperating)
        if(enemyLastMove == Action.COOPERATE and myLastMove == Action.COOPERATE):
            self.pCoop += 1 / self.currRound
        #if punishment (enemy is cheating and I am cheating)
        if(enemyLastMove == Action.CHEAT and myLastMove == Action.CHEAT):
            self.pCoop -= 1 / self.currRound
        #if sucker (enemy is cheating and I am cooperating)
        if(enemyLastMove == Action.CHEAT and myLastMove == Action.COOPERATE):
            self.pCoop -= 2 / self.currRound
        #if temptation  (enemy is cooperating and I am cheating)
        if(enemyLastMove == Action.COOPERATE and myLastMove == Action.CHEAT):
            self.pCoop += 2 / self.currRound
        #clamp pCoop
        if(self.pCoop > 1):
            self.pCoop = 1
        if(self.pCoop < 0):
            self.pCoop = 0
        
        random = np.random.uniform(0, 1)
        if(random < self.pCoop):
            return Action.COOPERATE
        else:
            return Action.CHEAT
