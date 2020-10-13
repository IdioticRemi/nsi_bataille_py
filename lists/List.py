from random import randint

from cardgame.lists.Cell import Cell


class List:
    def __init__(self):
        self.__storage__ = None

    # Une sorte de getter à la JavaScript pour obtenir la taille de la list de manière "dynamique" et non "statique"
    @property
    def len(self):
        last = self.__storage__
        size = 0

        while last is not None:
            size += 1
            last = last.next

        return size

    # Vider le contenu de la liste
    def clear(self):
        self.__storage__ = None

        return True

    # Trouver la position d'un élément dans la liste, None est retourné si il n'existe pas
    def index(self, val):
        last = self.__storage__
        index = 0

        while last is not None:
            # Juste pour que l'index de qqch en position 0 fonctionne
            # Sah quel plaisir, flemme de faire un if au dessus x)
            # Ca servira de double vérification pour la peine même si
            # Ce n'est pas très optimisé
            if last.val == val:
                return index
            # Le reste...
            elif last.next is None:
                return None
            else:
                if last.next.val == val:
                    return index + 1
                else:
                    index += 1
                    last = last.next

        return None

    # Chercher si notre liste custom contiens un élément
    def has(self, val):
        last = self.__storage__

        while last is not None:
            if last.next is None:
                return None
            else:
                if last.next.val == val:
                    return True
                else:
                    last = last.next

        return False

    # Trouver l'élément si situant à un certain index et le routourner
    def at(self, pos):
        if pos is None or pos < 0:
            return None

        last = self.__storage__
        index = 0

        while index != pos:
            if last.next is None:
                return None
            else:
                index += 1
                last = last.next

        return last.val

    # Ajouter un élément au bout de notre système custom
    def push(self, val):
        last = self.__storage__

        if not last:
            self.__storage__ = Cell(val)
            return True

        while last is not None:
            if last.next is None:
                last.next = Cell(val)
                return True
            else:
                last = last.next

        return False

    # Insérer un élément à une certaine position dans notre liste custom
    def insert(self, val, pos):
        if pos < 0:
            return False

        last = self.__storage__
        index = 0

        if not last:
            self.__storage__ = Cell(val)
            return True

        while index != pos:
            if last.next is None:
                last.next = Cell(val)
                return True
            else:
                if not index == pos - 1:
                    last = last.next
                index += 1

        if index == 0:
            temp = last
            last = Cell(val)
            last.next = temp

            self.__storage__ = last
        else:
            temp = last.next
            last.next = Cell(val)
            last.next.next = temp

        return True

    # Supprimer le dernier élément et le retourner, comme avec les listes natives
    def pop(self):
        t = self.at(self.len - 1)
        self.delete(self.len - 1)
        return t

    # Supprimer un élément dans la liste
    def delete(self, pos):
        if pos < 0:
            return False

        last = self.__storage__
        index = 0

        if last is None:
            return True

        while last is not None and index != pos:
            if last.next is not None and last.next is None:
                last.next = None
                return True
            else:
                if not index == pos - 1:
                    last = last.next
                index += 1

        if index == 0:
            self.__storage__ = last.next
        else:
            last.next = last.next.next

        return True

    # Mélanger toutes les valeurs de la liste
    def shuffle(self, passes=1):
        for _ in range(passes):
            temp = List()
            while self.len > 0:
                i = randint(0, self.len - 1)
                temp.push(self.at(i))
                self.delete(i)

            self.__storage__ = temp.__storage__

    # Ajouter le contenu d'une liste dans notre système custom
    def from_array(self, arr):
        while len(arr) > 0:
            self.push(arr.pop(0))

        return True

    # Transformer cette chaine de variables en une array python native
    # De façon à pouvoir effectuer des itérations dans le contenu avec les opérateurs for et in
    def to_array(self):
        last = self.__storage__
        arr = []

        while last is not None:
            arr.append(last.val)

            last = last.next

        return arr

    # Juste pour faire plus professionnel visuellement haha
    @property
    def iter(self):
        return self.to_array()
