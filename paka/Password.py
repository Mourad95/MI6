#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import paka.commons
import paka

def spanker_code():
    print("*********************CODE***********************")
    print("\n\n")
    password_interface()


def change_passw():  # Fonction pour changer le mot de passe
    ok = False  # Variable de sortie de la boucle
    while not ok:  # Boucle de securite
        psw_temp = input("ENTER THE NEW PASSWORD: ")  # Stockage de l'entre utilisateur
        psw_len = len(psw_temp)  # Stockage de la longueur de l'entree utilisateur
        if psw_len >= 3 and psw_len <= 8:  # Verification des conditions de longueur du mot de passe
            psw = psw_temp  # Si conditions remplie, le changement est effectue
            password(psw)
            ok = True  # Changement de la variable ok pour pouvoir sortir de la boucle
        else:  # En cas de reponse incorrecte de l'utilisateur
            print("INCORRECT // TRY AGAIN")
    return ok  # Envoie de ok en true pour sortir de la boucle superieur


def password(psw):
    essaie = 3  # Nombre d'essaies avant fin du programme
    ok = False  # Variable de sortie de la boucle
    while not ok:  # Boucle de securite
        user_pass = input("ENTER PASSWORD : ")  # Recuperation de l'entree utilisateur
        if psw == user_pass:  # Verefication de l'entree utilisateur par rapport au mot de passe
            print("CORRECT ANSWER // YOU CAN ENTER\nAT YOUR OWN RISK\n\n")
            essaie = 3  # Reinitialisation d'essaie
            ok = paka.commons.pc_menu()  # ok prend la valeur que renvoie pc_menu
        else:  # En cas de response incorrecte de l'utilisateur
            if essaie > 1:  # message si le nombre d'essaie est superieur a 1
                print("WRONG PASSWORD // TRY AGAIN\nYOU HAVE", essaie, "ATTEMPTS LEFT")
            elif essaie == 1:  # message si le nombre d'essaie est egal a 1
                print("WRONG PASSWORD // TRY AGAIN\nLAST ATTEMPT")
            elif essaie <= 0:  # message si nombre d'essaie epuise + sortie de boucle
                print("/!\ ERROR /!\ \nPROGRAM SHUTDOWN")
                ok = True
            essaie -= 1  # Compteur d'essaie


def password_interface():

    password("admin")
