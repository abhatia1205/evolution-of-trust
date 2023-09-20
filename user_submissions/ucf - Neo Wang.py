from Util import Action, PAYOFF, ROUNDS
from Player import Player
'''
Action enum for valid moves:
	Action.CHEAT
	Action.COOPERATE
You can access the payoff matrix with PAYOFF
You can access the number of rounds between two people with ROUNDS
'''
from enum import Enum
class Action(Enum):
	CHEAT = 0
	COOPERATE = 1

PAYOFF = [[0, 3],
		[-1, 2]]
REPRODUCE = 15 #
ROUNDS = 10
GAMES = 50
NOISE = 0.05

class Example(Player):
	'''This class implements your strategy.
	Don't make your own __init__
	Make sure to change the file name and class name
	You are provided with two fields:
		self.self_history : List[Action]
			List of Actions you have taken this game, after noise mutations
		self.other_history : List[Action]
			List of Actions your opponent has taken this game, after noise mutations
	
	If you want to keep a list of your own actions without noise mutations,
	do so yourself.
	'''
	def initialize(self) -> None:
		''' Feel free to create your own fields here.
		'''
		self.dummy_string = ""

	def act(self) -> Action:
		if(len(self.other_history) == 0): #Cooperates first time
			return Action.CHEAT

		# self.other_history
		# calculate EV of other history

		cheat_prob = 0
		tot_prob = 0
		
		# weight recency more
		for i, action in enumerate(self.other_history):
			if action == Action.CHEAT:
				cheat_prob += i
			tot_prob += i 

		# calculate ev
		# if they cheat with high probability, we should cheat
		# if they cooperate, choose to cooperate
		prob = cheat_prob / tot_prob
		
		ev_cheat = 3 * (1 - prob)
		ev_cooperate = -1 * prob + 2 * (1 - prob)

		if ev_cheat >= ev_cooperate:
			return Action.CHEAT
		else:
			return Action.COOPERATE

	
	'''
	Update any kept state variables after standoff between two players.
	The standoff's results are added in self.other_history and self.self_history.
	'''
	
	def update(self) -> None:
		self.dummy_string += 'a'