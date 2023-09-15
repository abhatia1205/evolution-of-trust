from typing import List
from Player import Player
from Submissions import *
import glob

def genPlayers() -> List[Player]:
    classNames = [c[14:-3] for c in glob.glob('./Submissions/*.py') if not '__init__.py' in c]
    print(classNames)
    players = []
    for c in classNames:
        players.append(getattr(globals()[c], c)())
    return players