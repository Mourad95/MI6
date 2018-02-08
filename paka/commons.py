#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import paka.Media
import paka.Password
import paka.CompteARebour
import threading
import tkinter

import time
import subprocess

main = tkinter.Tk()
txt = tkinter.Text(main)
txt.grid()


def spanker_face():              # Interface Spanker
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("             ███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█")
    print("             ████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█")
    print("             ███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
    print("             ████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
    print("             ███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█")
    print("             ████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█")
    print("             ███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
    print("             ████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
    print("             ███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
    print("             █████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
    print("             █████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██")
    print("             █████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██")
    print("             ████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██")
    print("             ████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██")
    print("             █████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██")
    print("             █████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███")
    print("             ██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███")
    print("             ███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████")
    print("             ███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████")
    print("             ████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████")
    print("             █████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████")
    print("             ██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓███████")
    print("             ███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████")
    print("             ██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████")
    print("             ███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████")
    print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(5)
    print("CHARGEMENT EN COUR PLEASE WAIT....LOADING")
    time.sleep(3)
    paka.Media.chargement_call_and_kill()
    print("\n\n")
    paka.Password.spanker_code()


def pc_menu():  # Fonction de gestion du menu
    ok = False  # Variable de sortie de la boucle
    while not ok:  # Boucle de securite
        choix = input("CHOOSE:\n1.ENTER THE SYSTEM\n2.CHANGE PASSWORD\n3.QUIT\n\n")  # Stockage de l'entree utilisateur
        if choix == '1':  # Si choix 1 selectionne, on accede à la suite du programme
            paka.CompteARebour.entree_system()
        elif choix == '2':  # Si choix 2 selectionne, acces à la fonction de changement de mot de passe
            ok = paka.Password.change_passw()
        elif choix == '3':  # Si choix 3 selectionne, sortie de la fonction pc_menu et
                            # renvoie de ok pour sortie de boucle supérieur
            print("GOOD BYE <3")
            ok = True
        else:  # Si la réponse de l'utilisateur ne correspond a rien, la boucle continue
            print("INCORRECT // TRY AGAIN")
    return ok  # Renvoie de ok pour sortir de la boucle superieur



















