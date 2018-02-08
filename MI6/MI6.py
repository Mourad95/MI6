#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import os
import time
import sys
try:    # Tentative d'import de tty et termios / systeme UNIX
    import tty
    import termios
except ImportError:  # Si la tentative echoue, probablement systeme Windows.
    try:
        import msvcrt
    except ImportError:
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():  # Creation du getch sous systeme Unix
        file_descriptor = sys.stdin.fileno()
        old_settings = termios.tcgetattr(file_descriptor)
        try:
            tty.setraw(file_descriptor)
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
        return char


alphabet_min_tuple = (('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u','v', 'w', 'x','y', 'z'))
alphabet_min = ''.join(alphabet_min_tuple)
majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decodage_texte(message_code, valeur_de_decalage):  # Décode une chaine de caractere quelconque.

    alph_deca_min = decalage(alphabet_min_tuple, valeur_de_decalage)  # Stockage de la fonction decalage dans la variable
    alph_deca_maj = decalage(majuscules, valeur_de_decalage)  # Stockage de la fonction decalage dans la variable
    resultat = ''
    for i_lettre in message_code:
        if i_lettre in alphabet_min_tuple:
            resultat = resultat + alphabet_min[index_lettre(i_lettre, alph_deca_min)]
        elif i_lettre in majuscules:
            resultat = resultat + majuscules[index_lettre(i_lettre, alph_deca_maj)]
        else:
            resultat = resultat + i_lettre
    return resultat


def decalage(alphabet_min, valeur_de_decalage):  # Permet d'effectuer un slice sur l'alphabetMin.

    return alphabet_min[valeur_de_decalage:] + alphabet_min[:valeur_de_decalage]


def index_lettre(lettre, message):  # Retourne l'index de la lettre choisi dans
                                    # la chaine de charactere passez en argument.
    for i in range(len(message)):
        if (lettre == message[i]):
            return i
    return -1


def clear():  # Fonction pour clear le terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def _print(string):     # Fonction pour eviter que print soit retenu par sleep
    sys.stdout.write(string)
    sys.stdout.flush()


def mi6_connection():   # Fonction d'affichage de connection
    _print("CONNECTION PLEASE WAIT")
    time.sleep(1)
    for x in range(0, 5):
        _print(".")
        time.sleep(2)
    _print("\nCONNECTION ESTABLISHED\n")
    time.sleep(2)
    clear()


def aff_mi6(pos):  # Fonction d'affichage, prend en compte la position du curseur avec la variable pos
    print("*------------------------------------------------------------------------------------------*")
    print("| MI6 AGENT WELCOME                                                                        |")
    print("| WHAT TOOL YOU WANT TO USE TODAY ?                                                        |")
    print("| USE ARROW UP AND DOWN TO MOVE THE CURSOR                                                 |")
    print("| USE ENTER TO SELECT                                                                      |")
    print("|                                                                                          |")
    print("|                                                                                          |")
    if pos == 1:
        print("| > 1. CODENAME: DECODER (USAGE: POSSIBLE)                                                 |")
    else:
        print("|   1. CODENAME: DECODER (USAGE: POSSIBLE)                                                 |")
    if pos == 2:
        print("| > 2. CODENAME: TERMINATOR (USAGE: NOT POSSIBLE CONNECTION TOO LOW)                       |")
    else:
        print("|   2. CODENAME: TERMINATOR (USAGE: NOT POSSIBLE CONNECTION TOO LOW)                       |")
    if pos == 3:
        print("| > 3. CODENAME: SNOW STORM  (USAGE: ALREADY IN USE)                                       |")
    else:
        print("|   3. CODENAME: SNOW STORM  (USAGE: ALREADY IN USE)                                       |")
    if pos == 4:
        print("| > 4. CODENAME: THE ANSWER TO LIFE, THE UNIVERSE AND EVERYTHING ELSE (USAGE: POSSIBLE)    |")
    else:
        print("|   4. CODENAME: THE ANSWER TO LIFE, THE UNIVERSE AND EVERYTHING ELSE (USAGE: POSSIBLE)    |")
    if pos == 5:
        print("| > 5. CODENAME: DEATH RAY (USAGE: ALREADY IN USE ELSEWHERE)                               |")
    else:
        print("|   5. CODENAME: DEATH RAY (USAGE: ALREADY IN USE ELSEWHERE)                               |")
    if pos == 6:
        print("| > 6. QUIT                                                                                |")
    else:
        print("|   6. QUIT                                                                                |")
    print("|                                                                                          |")
    print("|                                                                                          |")
    print("| REMEMBER THIS OFFICIALY DON'T EXIST                                                      |")
    print("| USE AT YOUR OWN RISK                                                                     |")
    print("*------------------------------------------------------------------------------------------*")


def menu_selec(pos):
    ok = False
    while not ok:  # Boucle de securite
        clear()
        if pos == 1:  # Position 1 correspondant au decoder
            print(decodage_texte(input("Entrer le message codé : "), int(input("Valeur de décryptage :"))))
            time.sleep(5)
            ok = True
        elif pos == 2:  # Position 2 correspondant a une fausse reponse
            print("WARNING: CONNECTION TOO LOW TO GARANTY SAFE USAGE")
            time.sleep(2)
            ok = True
        elif pos == 3:  # Position 3 correspondant a une fausse reponse
            print("WARNING: SNOW STORM ALREADY IN USE IN YOUR AREA")
            time.sleep(2)
            ok = True
        elif pos == 4:  # Position 4 correspondant a une fausse reponse
            print("42")
            time.sleep(2)
            ok = True
        elif pos == 5:  # Position 5 correspondant a une fausse reponse
            print("WARNING: DEATH RAY CAN'T BE USED BY TWO PERSON AT THE SAME TIME")
            time.sleep(2)
            ok = True
        elif pos == 6:  # Position 6 correspondant à la sortie du programme
            print("GOOD BYE AND GOOD LUCK AGENT")
            time.sleep(2)
            ok = True
        else:  # En cas de réponse non prevu, sortie de boucle
            print("FATAL ERROR // SYSTEM SHUTDOWN")
            time.sleep(2)
            ok = True


def unix_pos(pos, char):
    if ord(char) == 27:  # Correspond au premier caractere des touches clavier fleche haut/bas
        getch()  # Passage du second symbole car similaire entre les deux fleches clavier
        char = getch()  # Recuperation du dernier caractere qui determine la difference entre les fleches
        if ord(char) == 65:     # Si fleche haut est appuyer, le curseur monte,
                                # s'il est en haut du menu il repasse en bas
            pos -= 1
            if pos == 0:
                pos = 6
        elif ord(char) == 66:   # Si fleche du bas est appuyer, le curseur descend,
                                # s'il est tout en bas du menu il repasse en haut
            pos += 1
            if pos == 7:
                pos = 1
    return pos


def ms_pos(pos, char):
    if ord(char) == 224:  # Correspond au premier caractere des touches clavier fleche haut/bas
        char = getch()  # Recuperation du second caractere qui differencie les deux fleches clavier
        if ord(char) == 72: # Si fleche haut est appuyer, le curseur monte,
                            # s'il est en haut du menu il repasse en bas
            pos -= 1
            if pos == 0:
                pos = 6
        elif ord(char) == 80:   # Si fleche du bas est appuyer, le curseur descend,
                                # s'il est tout en bas du menu il repasse en haut
            pos += 1
            if pos == 7:
                pos = 1
    return pos


def mi6_screen():   # Fontion principal de l'écran du MI6
    ok = False      # Variable de sortie de boucle
    pos = 1         # Variable de positionnement du curseur, par defaut est egal a 1
    mi6_connection()
    while not ok:       # Boucle de sécurité
        aff_mi6(pos)    # Affichage du menu
        char = getch()  # Recuperation du caractere en appuyant sur une touche clavier
        if os.name == 'nt':     # Si l'os est sur base microsoft
            pos = ms_pos(pos, char)
        else:
            pos = unix_pos(pos, char)     # Si l'os est sur base unix
        if ord(char) == 13:   # Si entrer est appuye, la fonction de selection est appelee
            menu_selec(pos)
            if pos == 6:
                ok = True
        clear()  # Fonction pour clear le terminal


def main():
    mi6_screen()


if __name__ == '__main__':
    main()