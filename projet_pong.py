#!/usr/bin/python3

import os
from tkinter import *

#fonction balle
def gameTick():
    global dx, dy
    coord = canvas.coords(balle)
    if (coord[1] >= (hauteur-10)) or (coord[3] <= 10):
        dy *= -1
    if (coord[0] <= 0) or (coord[2] >= largeur):
        dx *= -1
    canvas.move(balle, dx, dy)
    fenetre.after(15, gameTick)

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

#creation balle
balle = canvas.create_oval((largeur / 2) -5 , (hauteur / 2) - 5, (largeur / 2) + 5, (hauteur / 2) + 5, fill = 'white')

#vitesse balle
dx = 3
dy = 3

#ligne vertical
ligne_vertical = canvas.create_line((largeur / 2), 0, (largeur / 2), hauteur, fill = "white", dash = (10, 5))

#boucle infinie
gameTick()
fenetre.mainloop()