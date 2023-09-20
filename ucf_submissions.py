from typing import Type, List, Tuple
from Player import Player
from user_submissions import *
import glob
import inspect
import importlib
from Util import * 

from Game import Game

def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

def genClasses() -> List[Tuple[str, Type[Player]]]:
    '''Generates of a list of classes in the Submissions package

    Returns:
        List[Tuple[str, Type[Player]]] - List of tuples with pairs of class name and classes
    '''
    moduleNames = [c[19:-3] for c in glob.glob('./user_submissions/*.py') if not '__init__.py' in c]
    # print(moduleNames)
    players = []
    player_dict = {}
    for c in moduleNames:
        for name, klass in inspect.getmembers(globals()[c], inspect.isclass):
            print(klass.__module__)
            if 'user_submissions' in klass.__module__ and issubclass(klass, Player):
                # my_import('Submissions.'+c+'.'+name)
                SubmissionClass = getattr(importlib.import_module('user_submissions.'+c), name)
                print(SubmissionClass)
                player_dict[SubmissionClass] = 5
                players.append((c+'.'+name, klass))
    print(player_dict)
    return player_dict


def main():
    player_dict = genClasses()
    g = Game(player_dict)
    g.print_players()
    g.game()

if __name__ == '__main__':
    main()