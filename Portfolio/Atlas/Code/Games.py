import random
from random import choice
from unidecode import unidecode


########################################################################################################################

# Choix du Jeu

def choix_jeux():
    print("\nVous avez le choix entre ces différents jeux mon ami ! (Entrez le chiffre de sélection)")
    print("1. Pendu")
    print("2. Pierre-Papier-Ciseaux")
    print("3. Devine le chiffre")
    print("\n0. Revenir à la discussion\n")
    choix = int(input("You: "))

    return choix


def lancer_jeux(jeu):
    if jeu == 1:
        pendu()
    if jeu == 2:
        PPC()
    if jeu == 3:
        Guess_Number()


########################################################################################################################

# Jeu du Pendu

# Un mot au hasard
def word():
    f = open('../TXT/mots.txt', 'r', encoding='utf8')
    contenu = f.readlines()
    return unidecode(choice(contenu)).upper().replace('\n', '')


# Remplacement par des underscores
def underscore(mot, L=[]):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '

    return r[:-1]


# Saisie d'une lettre
def saisie():
    lettre = input('Entrez une lettre : ')
    if len(lettre) > 1 or ord(lettre) < 65 or ord(lettre) > 122:
        return saisie()
    elif "quit" in lettre:
        return 0
    else:
        return lettre.upper()


# Choix de la difficulté
def choice_diff_Pendu():
    print(
        "Choisissez votre difficultée ! (entrez le chiffre) \n1.Easy (10 essais)\n2.Medium (6 essais) \n3.Hard (4 "
        "essais)\n")
    inp = int(input("You (Player): "))
    if inp == 1:
        nb = 11
    elif inp == 2:
        nb = 7
    elif inp == 3:
        nb = 5
    else:
        print("N'entrez que le chiffre à sélectionner")

    return nb


# Programme principal
def pendu():
    print("\n###########################")
    print("#Bienvenu dans le Pendu !#")
    print("##########################\n")

    diff = choice_diff_Pendu()
    lettres_deja_proposees = []
    lettres_deja_proposees.clear()
    mot_a_deviner = word()

    affichage = underscore(mot_a_deviner)
    print('Mot à deviner : ', affichage)

    nb_erreurs = 0

    while '_' in affichage and nb_erreurs < diff:
        lettre = saisie()

        # if lettre == 0:
        # nb_erreurs += 100

        if lettre not in lettres_deja_proposees:
            lettres_deja_proposees.append(lettre)

        if lettre not in mot_a_deviner:
            nb_erreurs += 1

        # if lettre in lettres_deja_proposees:
        # print("Lettre deja proposée !")

        affichage = underscore(mot_a_deviner, lettres_deja_proposees)
        print('\nMot à deviner : ', affichage, ' ' * 10, 'Nombre d\'erreurs maximum :', diff - nb_erreurs)

        if nb_erreurs == diff:
            print("\nGAME OVER")
            print("Le bon mot était : " + mot_a_deviner + "\n")

    if nb_erreurs < diff:
        print("Bien joué !\n")


########################################################################################################################

# Jeu du Pierre Feuille Papier Ciseaux

# Programme principale
def PPC():
    print("\n####################################################################")
    print("#Bienvenu dans le Pierre-Papier-Ciseaux ! (Taper quit pour quitter)#")
    print("####################################################################\n")

    print("Entrez une première valeur\n")

    # liste des options
    jeu = ["pierre", "papier", "ciseaux"]

    # Attribuer une option aléatoire à l'ordinateur
    ordinateur = jeu[random.randint(0, 2)]

    # Gardez le compte des points
    points_joueur = 0
    points_ordinateur = 0

    continuer = True

    # La boucle continue jusqu'à ce que la variable continuer est fausse
    while continuer:
        # Demander le choix de l'ordinateur<br>
        joueur = input("You (Player): ")

        # Vérification des scenarios
        if joueur == 'quit':
            continuer = False
        elif joueur.lower() == ordinateur:
            print("Égalité!")
        elif joueur.lower() == "pierre":
            if ordinateur == "papier":
                print("Perdu!", ordinateur, "recouvre", joueur)
                points_ordinateur = points_ordinateur + 1
            else:
                print("Gagné!", joueur, "écrase", ordinateur)
                points_joueur = points_joueur + 1
        elif joueur.lower() == "papier":
            if ordinateur == "ciseaux":
                print("Perdu!", ordinateur, "cut", joueur)
                points_ordinateur = points_ordinateur + 1
            else:
                print("You win!", joueur, "recouvre", ordinateur)
                points_joueur = points_joueur + 1
        elif joueur.lower() == "ciseaux":
            if ordinateur == "Rock":
                print("Perdu...", ordinateur, "écrase", joueur)
                points_ordinateur = points_ordinateur + 1
            else:
                print("Gagné!", joueur, "cut", ordinateur)
                points_joueur = points_joueur + 1
        else:
            print("Votre choix n'est pas correct, vérifiez l'orthographe!")

        # Attribuer une option aléatoire à l'ordinateur
        ordinateur = jeu[random.randint(0, 2)]
        print('\n********Tour suivant********\n')

    # Impression des points
    print("\n********Points********\n")
    print("joueur: ", points_joueur)
    print("ordinateur: ", points_ordinateur, "\n")


########################################################################################################################

# Jeu du Chiffre

# Programme du choix de la difficulté
def choice_diff_chiffre():
    print("Choisissez votre difficultée ! (entrez le chiffre) \n1.Easy (0-50)\n2.Medium (0-100) \n3.Hard (0-200)\n")
    inp = int(input("You (Player): "))
    if inp == 1:
        nb = 50
    elif inp == 2:
        nb = 100
    elif inp == 3:
        nb = 200
    else:
        print("N'entrez que le chiffre à sélectionner")

    return nb


# Programme Principale
def Guess_Number():
    print("\n#################################")
    print("#Bienvenu dans le Guess Number !#")
    print("#################################\n")

    # Choix du max
    upper = choice_diff_chiffre()

    # Génération aléatoire du chiffre entre 0 et le max
    x = random.randint(0, upper)

    print("\n\tVous n'avez que 10 chances pour trouver le bon nombre!\n")

    # Initialisation du nombre d'essais
    count = 0

    while count < 10:
        count += 1

        try:
            guess = int(input("Tentez un nombre: - "))
        except ValueError:
            print("Ce n'est pas un nombre désolé !")
            count -= 1

        if x == guess:
            print("Bien joué, vous avez trouvé en ", count, " coups \n")
            break

        # elif x == 0:
        #    print("Dommage !")
        #    break

        elif x > guess:
            print("Trop petit !")
        elif x < guess:
            print("Trop haut !")

    if count >= 10:
        print("\nLe nombre était : ", x)
        print("\tVous aurez plus de chances la prochaines fois !\n")
