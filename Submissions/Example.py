from Util import Action
from Player import Player

'''
Action enum for valid moves:
    Action.CHEAT
    Action.COOPERATE
'''

class Example(Player):
    '''This class implements your strategy

    Make sure to change the file name

    You are provided with two fields:
        self.self_history : List[Action]
            List of Actions you have taken this game
        self.other_history : List[Action]
            List of Actions your opponent has taken this game
    '''
    def __init__(self) -> None:
        ''' Feel free to create your own fields here
        '''
        super().__init__()

    def act(self) -> Action:
        '''Performs logic to determine next action

        Returns:
            Action
        '''
        return Action.CHEAT