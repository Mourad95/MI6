#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import subprocess
import threading
import paka


event = threading.Event()


def music_kim():  # Methode lancement music
    subprocess.call(["afplay", "psy.wav"])


def lancement_music():
    thread = threading.Thread(target=music_kim, args=(event,))  # Creation d'un thread pour la music
    thread.start()  # Lancement du Thread
