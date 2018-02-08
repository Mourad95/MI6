code ="Libererrrrrrr delivrerrrrrrrr je ne mentirai plus jamaiiiiiiiiiiss, je voudrais un bonhomme de neige!!!"
alphabetMin1 = (('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z'))
alphabetMin = ''.join(alphabetMin1)
majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = 2



def decalage(alphabetMin, x):  # Permet d'effectuer un slice sur l'alphabetMin.

    return alphabetMin[x:] + alphabetMin[:x]


def indexLettre(c, chaine):  # Retourne l'index de la lettre choisi dans la chaine de charactere passez en argument.

    for i in range(len(chaine)):
        if (c == chaine[i]):
            return i
    return -1


def codageMessage(chaineDeCharactere,
    nombreDeDecalage):  # Chiffre une chaine de charactere en lui passant en parametre de combien
                        # veut on que l'alphabetMin soit décalé;
    r = decalage(alphabetMin,nombreDeDecalage)  # r est valoriser par le retour de la méthode decalage c'est a dire par un alphabet décaler.
    resultat = ''  # Initialisation de la variable résultat.
    for iLettre in chaineDeCharactere:
        resultat = resultat + r[indexLettre(iLettre,
                                            alphabetMin)]  # La methode indexLettre retourne l'index des lettre de alphabetMin a l'alphabet décalé
    return resultat


def encodageMessage(chaineDeCharactere, nombreDeDecalage):  # Decodage de la fonction codageMessage.
    r = decalage(alphabetMin, nombreDeDecalage)
    resultat = ''
    for iLettre in chaineDeCharactere:
        resultat = resultat + alphabetMin[indexLettre(iLettre, r)]
    return resultat


def codageTexte(chaineDeCharactere, x):  # Code une chaine de caractere quelconque.
    r_min = decalage(alphabetMin1, x)
    r_maj = decalage(majuscules, x)
    resultat = ''
    for lettre in chaineDeCharactere:
        if lettre in alphabetMin1:
            resultat = resultat + r_min[indexLettre(lettre, alphabetMin1)]
        elif lettre in majuscules:
            resultat = resultat + r_maj[indexLettre(lettre, majuscules)]
        else:
            resultat = resultat + lettre
    return resultat


def encodageTexte(chaineDeCharactere, x):  # Décode une chaine de caractere quelconque.

    r_min = decalage(alphabetMin1, x)
    r_maj = decalage(majuscules, x)
    resultat = ''
    for iLettre in chaineDeCharactere:
        if iLettre in alphabetMin1:
            resultat = resultat + alphabetMin[indexLettre(iLettre, r_min)]
        elif iLettre in majuscules:
            resultat = resultat + majuscules[indexLettre(iLettre, r_maj)]
        else:
            resultat = resultat + iLettre
    return resultat

messageCoder=(codageTexte("Libererrrrrrr delivrerrrrrrrr je ne mentirai plus jamaiiiiiiiiiiss, je voudrais un bonhomme de neige!!!",2))
print(messageCoder)
print(encodageTexte(messageCoder,2))