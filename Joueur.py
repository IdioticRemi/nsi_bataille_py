from cardgame.Carte import Carte
from cardgame.lists.List import List


class Joueur:
    name: str = None
    perdu: bool = False

    cartes: [Carte] = List()

    def __init__(self, name):
        self.name = name
        self.perdu = False
        self.cartes = List()
