#!/usr/bin/python3

import os
from tkinter import *
from tkinter import font

#canvas
fenetre = Tk()
largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()
resolution = str(largeur) + 'x' + str(hauteur)
fenetre.geometry(resolution)
canvas = Canvas(fenetre, width = largeur, height = hauteur, bg = 'black')
canvas.pack()

#fenetre
fenetre.title("Pong")
fenetre.attributes('-fullscreen', 1)

#composants
canvas.grid(row = 3, column = 3, rowspan = 2, columnspan = 3)
btn_jouer = Button(fenetre, text = 'Jouer', command = 'jouer', width = 20)
btn_quitter = Button(fenetre, text = 'Quitter', command = fenetre.destroy, width = 20)
btn_jouer.grid(row = 2, column = 3, rowspan = 2, columnspan = 3)
btn_quitter.grid(row = 3, column = 3, rowspan = 3, columnspan = 3)

#boucle infinie
fenetre.mainloop()