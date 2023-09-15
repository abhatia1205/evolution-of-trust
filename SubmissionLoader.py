from typing import Type, List, Tuple
from Player import Player
from Submissions import *
import glob
import inspect

def genClasses() -> List[Tuple[str, Type[Player]]]:
    '''Generates of a list of classes in the Submissions package

    Returns:
        List[Tuple[str, Type[Player]]] - List of tuples with pairs of class name and classes
    '''
    moduleNames = [c[14:-3] for c in glob.glob('./Submissions/*.py') if not '__init__.py' in c]
    print(moduleNames)
    players = []
    for c in moduleNames:
        for name, klass in inspect.getmembers(globals()[c], inspect.isclass):
            if 'Submissions' in klass.__module__ and issubclass(klass, Player):
                players.append((c+'.'+name, klass))
    return players

players = genClasses()
print(players)