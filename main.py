from cardgame.Bataille import Bataille
from cardgame.color import Color
from cardgame.lists.List import List

print("Jeu de cartes (Bataille)")
print()

# Création du Jeu

jeu = Bataille()

# Mélange des cartes

jeu.cartes.melanger()

# Création des joueurs

ended = False

while not ended:
    # Les deux premiers joueurs sont obligatoires (bah sinon on peut juste pas jouer quoi...)
    while jeu.joueurs.len < 2:
        nom = ""
        while nom == "":
            nom = input("Nom du joueur? ")

        jeu.creer_joueur(nom)

    # Système d'ajout jusqu'a 4 joueurs
    while 2 <= jeu.joueurs.len < 4 and not ended:
        newPlayer = ""
        while newPlayer == "":
            tmp = input("Voulez vous créer un autre personnage? (O/N) ")
            if tmp.lower() == "o":
                newPlayer = True
            elif tmp.lower() == "n":
                newPlayer = False

        if newPlayer:
            nom = ""
            while nom == "":
                nom = input("Nom du joueur? ")

            jeu.creer_joueur(nom)
        else:
            ended = True

    ended = True

# Joueurs test

# jeu.joueurs = List()
# jeu.joueurs.from_array([Joueur("Océanne"), Joueur("Thomas"), Joueur("Sabrine"), Joueur("Tom")])

# Distribution équitable des cartes

x = 0
while jeu.cartes.cartes.len > 0:
    c = jeu.cartes.cartes.pop()
    pi = x % jeu.joueurs.len

    jeu.joueurs.at(pi).cartes.push(c)

    x += 1

# Commencer la partie

winner = None
manche = 0

# Boucle principale du jeu

while winner is None:
    # Un joueur a gagné?
    for i in range(jeu.joueurs.len - 1):
        if jeu.joueurs.at(i).cartes.len == 52:
            winner = i
            break

    # Exécution de la manche en cours

    cartesEnJeu = List()
    logs = List()

    mancheWinner = None
    carteWinner = None

    nope = List()
    oponents = List()
    bataille = False

    # Boucle tant qu'on a pas de gagnant pour la manche
    # Note: le système de bataille est intégré donc par exemple:
    # Si deux joueurs ont la même carte, ils en posent une face cachée
    # Puis se rebattent avec la carte suivante
    # Et ainsi de suite jusqu'a qu'on ait un vainqueur
    # Ou jusqu'a que l'un des deux n'ait plus de cartes

    while mancheWinner is None:
        for p in jeu.joueurs.iter:
            # Le joueur n'as plus de cartes?
            if not p.perdu and p.cartes.len == 0:
                p.perdu = True
                logs.push(f"{Color.FAIL}DEFAITE{Color.ENDC}: {p.name} (Plus de cartes)")
            else:
                # Si on sors d'une bataille, on pose chacun une carte face cachée puis on lance l'execution suivante
                if cartesEnJeu.len != 0 and bataille is True:
                    bataille = False
                    for pl in jeu.joueurs.iter:
                        if pl.cartes.len > 0 and jeu.joueurs.index(pl) in oponents.iter:
                            cartesEnJeu.push(pl.cartes.pop())
                    break
                if p.cartes.len > 0 and jeu.joueurs.index(p) not in nope.iter:
                    # Le joueur a une meilleure carte que le plus fort de la manche?
                    carteJoueur = p.cartes.pop()
                    logs.push(f"{p.name} joue: {carteJoueur.name}")
                    if not carteWinner or carteWinner.valeur < carteJoueur.valeur:
                        mancheWinner = jeu.joueurs.index(p)
                        carteWinner = carteJoueur
                    cartesEnJeu.push(carteJoueur)

                    # Le joueur a la même carte que le plus fort de la manche?
                    if mancheWinner != jeu.joueurs.index(p) and carteWinner.valeur == carteJoueur.valeur:
                        oponents = List()
                        oponents.push(mancheWinner)
                        oponents.push(jeu.joueurs.index(p))

                        for pl in jeu.joueurs.iter:
                            if jeu.joueurs.index(pl) not in oponents.iter:
                                nope.push(jeu.joueurs.index(pl))

                        mancheWinner = None
                        carteWinner = None
                        bataille = True

                        logs.push(f"{Color.DEBUG}BATAILLE{Color.ENDC}: {jeu.joueurs.at(oponents.at(0)).name} "
                                  f"{Color.DEBUG}VS{Color.ENDC} "
                                  f"{jeu.joueurs.at(oponents.at(1)).name}!{Color.ENDC}")
                        break

    # On donne les cartes mises en jeu au gagnant
    cartesEnJeu.shuffle()

    for carte in cartesEnJeu.iter:
        jeu.joueurs.at(mancheWinner).cartes.insert(carte, 0)

    # Affichage du récapitulatif de la manche
    print(f"\n{Color.OKGREEN}Récapitulatif de la manche #{manche}:{Color.ENDC}\n")

    for log in logs.iter:
        print(log)

    print(f"\n{Color.OKBLUE}{jeu.joueurs.at(mancheWinner).name} est le gagnant de la manche et il remporte "
          f"{cartesEnJeu.len} cartes!{Color.ENDC}\n")
    for p in jeu.joueurs.iter:
        if not p.perdu:
            print(f"{p.name} a {p.cartes.len} cartes.")

    # On a un gagnant?
    losers = 0
    for p in jeu.joueurs.iter:
        if p.perdu:
            losers += 1

    if losers == jeu.joueurs.len - 1:
        for p in jeu.joueurs.iter:
            if not p.perdu:
                winner = jeu.joueurs.index(p)

    if winner is None:
        # Attente prochaine manche
        input(f"\n{Color.WARNING}Faire entrer pour passer à la mache suivante...{Color.ENDC}\n")
        print("\n" * 5)

        manche += 1

print(f"\n\n{Color.BOLD}{Color.UNDERLINE}{jeu.joueurs.at(winner).name} "
      f"a gagné la partie en {manche} manches!{Color.ENDC}")
