from cardgame.JeuDeCartes import JeuDeCarte
from cardgame.Joueur import Joueur
from cardgame.lists.List import List


class Bataille:
    joueurs: [Joueur] = List()
    cartes: JeuDeCarte = None

    def __init__(self):
        self.joueurs = List()
        self.cartes = JeuDeCarte()

    def creer_joueur(self, name):
        self.joueurs.push(Joueur(name))
