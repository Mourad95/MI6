#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import paka
import tkinter
import time
import paka.CodeCesar
import paka.Interface
import paka.Music
import paka.Media
main = tkinter.Tk()
txt = tkinter.Text(main)
txt.grid()

code = "Libererrrrrrr delivrerrrrrrrr je ne mentirai plus jamaiiiiiiiiiiss, je voudrais un bonhomme de neige!!!"


def compte_a_rebour():
    print("Vous disposez d'un seul essai pour décoder le texte suivant, sinon....le gros bouton rouge :) \n\n")
    print(paka.CodeCesar.codage_texte(code, 2))
    vals = ['INITIALISATION DE LA BOMBE','.','..','...','20','19','18','17','16','15','14','13','12','11','10 BOUGE TOI ^^ !','9','8','7','6','5','4','3','2','1','0']
    i = 0
    print("\n\nTexte décoder: ")
    encodage = input()
    if (encodage == code):
        print("Bien jouer")
    elif(encodage != code):
        while i < len(vals):
            txt.delete('1.0','end')
            txt.insert('1.0',vals[i])
            txt.update_idletasks()
            time.sleep(1)
            i=i+1
            if(i==len(vals)-1):
                 print('\n\nYou LooOOoose')
                 paka.Music.lancement_music()
                 time.sleep(2)
                 paka.Media.image_kim()


def entree_system():
    main.after(1000, compte_a_rebour)
    main.mainloop()
