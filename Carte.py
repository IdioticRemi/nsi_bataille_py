enum_famille = ["Coeur", "Carreau", "Treffle", "Pic"]
enum_valeur = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Reine", "Roi", "As"]


class Carte:
    famille: int = None
    valeur: int = None
    name: str = None

    def __init__(self, famille, valeur):
        self.famille = famille
        self.valeur = valeur
        self.name = f"{enum_valeur[self.valeur]} de {enum_famille[self.famille]}"

    # def text(self):
    #     return f"J'ai pour valeur {self.valeur} dans la famille {self.famille}\nDonc je suis: {self.name}"
