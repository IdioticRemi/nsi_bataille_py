from cardgame.Carte import Carte
from cardgame.lists.List import List


class JeuDeCarte:
    cartes: [Carte] = List()

    def __init__(self):
        self.cartes = List()
        self.__creer__()

    def __creer__(self):
        for f in range(4):
            for v in range(13):
                self.cartes.push(Carte(f, v))

    def melanger(self, passes=1):
        # Voir code dans le code de la classe List, déplacé par convénience.
        self.cartes.shuffle(passes)

        # Ancien système avec les listes
        # for _ in range(passes):
        #     for i in range(self.cartes.len - 1):
        #         j = randint(0, self.cartes.len - 1)
        #
        #         t = self.cartes[i]
        #         self.cartes[i] = self.cartes[j]
        #         self.cartes[j] = t

        # "Triche" avec l'ancien système
        # shuffle(self.cartes)
