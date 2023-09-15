from typing import List, Tuple
from Player import Player
from Submissions import *
import glob
import inspect

def genPlayers() -> List[Tuple[str, Player]]:
    classNames = [c[14:-3] for c in glob.glob('./Submissions/*.py') if not '__init__.py' in c]
    print(classNames)
    players = []
    for c in classNames:
        for name, klass in inspect.getmembers(globals()[c], inspect.isclass):
            if 'Submissions' in klass.__module__ and issubclass(klass, Player):
                players.append((c+'.'+name, klass()))
    return players

players = genPlayers()
print(players[0][0])
print(players[0][1].act())