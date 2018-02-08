#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

code = "Libererrrrrrr delivrerrrrrrrr je ne mentirai plus jamaiiiiiiiiiiss, je voudrais un bonhomme de neige!!!"
alphabet_min_tuple = (('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't','u', 'v', 'w', 'x','y', 'z'))
alphabet_min = ''.join(alphabet_min_tuple)
majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = 2


def decalage(alphabet_min, valeur_de_decalage):  # Permet d'effectuer un slice sur l'alphabetMin.
    return alphabet_min[valeur_de_decalage:] + alphabet_min[:valeur_de_decalage]


def index_lettre(lettre, message):  # Retourne l'index de la lettre choisi dans la chaine de caractere
    for i in range(len(message)):   # passez en argument.
        if (lettre == message[i]):
            return i
    return -1


def codage_message(message, index_decalage):
    # Chiffre une chaine de charactere en lui passant en parametre la valeur de décalage.
    alph_deca_min = decalage(alphabet_min, index_decalage)
    # alph_deca_min est valorisé par le retour de la méthode decalage c'est a dire par un alphabet décalé.
    resultat = '' # Initialisation de la variable résultat.
    for i_lettre in message:
        resultat = resultat + alph_deca_min[index_lettre(i_lettre, alphabet_min)]
        # La methode i_lettre retourne l'index des lettre de alphabet_min a l'alphabet décalé
    return resultat


def decodage_message(message, index_decalage):  # Decodage de la fonction codage_message.
    alph_deca_min = decalage(alphabet_min, index_decalage)
    resultat = ''
    for i_lettre in message:
        resultat = resultat + alphabet_min[index_lettre(i_lettre, alph_deca_min)]
    return resultat


def codage_texte(message, valeur_de_decalage):  # Code une chaine de caractere quelconque.
    alph_deca_min = decalage(alphabet_min_tuple, valeur_de_decalage)
    alph_deca_maj = decalage(majuscules, valeur_de_decalage)
    resultat = ''
    for lettre in message:
        if lettre in alphabet_min_tuple:
            resultat = resultat + alph_deca_min[index_lettre(lettre, alphabet_min_tuple)]
        elif lettre in majuscules:
            resultat = resultat + alph_deca_maj[index_lettre(lettre, majuscules)]
        else:
            resultat = resultat + lettre
    return resultat


def decodage_texte(message, valeur_de_decalage):  # Décode une chaine de caractere quelconque.

    alph_deca_min = decalage(alphabet_min_tuple, valeur_de_decalage)
    alph_deca_maj = decalage(majuscules, valeur_de_decalage)
    resultat = ''
    for i_lettre in message:
        if i_lettre in alphabet_min_tuple:
            resultat = resultat + alphabet_min[index_lettre(i_lettre, alph_deca_min)]
        elif i_lettre in majuscules:
            resultat = resultat + majuscules[index_lettre(i_lettre, alph_deca_maj)]
        else:
            resultat = resultat + i_lettre
    return resultat

