#!/usr/bin/python3

import os
from tkinter import *
from tkinter import font

# canvas
fenetre = Tk()
largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()
resolution = str(largeur) + 'x' + str(hauteur)
fenetre.geometry(resolution)
canvas = Canvas(fenetre, width = largeur, height = hauteur, bg = 'black')

# fenetre
fenetre.title("Pong")
fenetre.attributes('-fullscreen', 1)

# fonction balle
def gameBall():
    global dx, dy
    coord = canvas.coords(balle)
    if (coord[1] >= (hauteur - 10)) or (coord[3] <= 10):
        dy *= -1
    if (coord[0] <= 0) or (coord[2] >= largeur):
        dx *= -1
    canvas.move(balle, dx, dy)
    fenetre.after(15, gameBall)

# fonction rectangle
def clavier_haut(event):
    canvas.move(raquette_1, 0, -ry)

def clavier_bas(event):
    canvas.move(raquette_1, 0, ry)

def clavier_haut2(event):
    canvas.move(raquette_2, 0, -ry)

def clavier_bas2(event):
    canvas.move(raquette_2, 0, ry)

# creation balle
ball = canvas.create_oval 
balle = ball(((largeur / 2) - 5), ((hauteur / 2) - 5), ((largeur / 2) + 5), ((hauteur / 2) + 5), fill = 'white')

# creation raquettes
raq = canvas.create_rectangle
raquette_1 = raq((largeur / 30), ((hauteur / 2) - 30), ((largeur / 30) - 20), ((hauteur / 2) + 30), fill = 'white')
raquette_2 = raq((largeur - (largeur / 30)), ((hauteur / 2) - 30), (largeur - (largeur / 30) + 20), ((hauteur / 2) + 30), fill = 'white')

# vitesse balle
dy = 3
dx = 3


# mouvement rectangle
ry = 20

# lignes verticales
lign = canvas.create_line
ligne_vertical = lign((largeur / 2), 0, (largeur / 2), hauteur, fill = "gray80", dash = (10, 5))

# victoire
def victory():
    global dx, dy
    coord = canvas.coords(balle)
    victoire = canvas.create_text
    if (coord[0] or coord[2] > 0):
        victoire((largeur - 300), ((hauteur / 2) - (hauteur / 4)), text = "Victoire JOUEUR 1", fill = "white")
    if (coord[2] or coord[0] < largeur):
        victoire((largeur - 1700), ((hauteur / 2) - (hauteur / 4)), text = "Victoire JOUEUR 2", fill = "white")


# ajout touche
canvas.bind_all('<KeyPress-z>', clavier_haut)
canvas.bind_all('<KeyPress-Z>', clavier_haut)
canvas.bind_all('<KeyPress-s>', clavier_bas)
canvas.bind_all('<KeyPress-S>', clavier_bas)
canvas.bind_all('<Up>', clavier_haut2)
canvas.bind_all('<Down>', clavier_bas2)

# appel & boucle
gameBall()
victory()
canvas.pack()
fenetre.mainloop()
fenetre.destroy()