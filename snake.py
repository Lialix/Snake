from tkinter import *
from random import *


def move():
    test;
    global deplacement
    global score
    global labelScore
    global fruit
    global listeCompteur
    global registre
    global compteur
    global listeQueue
    global ancienDeplacement
    compteur += 1

    ancienDeplacement = deplacement
    fen.bind('<Key>', check)
    if deplacement == "q":
        can.move(teteSerpent, -50, 0)
    elif deplacement == "d":
        can.move(teteSerpent, 50, 0)
    elif deplacement == "z":
        can.move(teteSerpent, 0, -50)
    elif deplacement == "s":
        can.move(teteSerpent, 0, 50)

    registre.append(can.coords(teteSerpent))

    if can.coords(teteSerpent)[0] < 0 or can.coords(teteSerpent)[1] < 0 or can.coords(teteSerpent)[0] > 450 or \
            can.coords(teteSerpent)[1] > 450:
        end()
        return

    if can.coords(teteSerpent) == can.coords(fruit):
        score += 1
        compteur -= 1
        labelScore.destroy()
        labelScore = Label(fen, text="Score : " + str(score))
        labelScore.pack()
        listeCompteur.append(compteur)

    for i in listeQueue[0:int((len(listeQueue) - 1))]:
        if can.coords(teteSerpent) == can.coords(i):
            end()
            return

    for i in listeQueue:
        can.delete(i)

    for i in listeCompteur:
        nom = can.create_oval(registre[i][0], registre[i][1], registre[i][0] + 50, registre[i][1] + 50, fill="#70F047",
                              width=2)
        listeQueue.append(nom)

    for i in range(len(listeCompteur)):
        listeCompteur[i] += 1

    if can.coords(teteSerpent) == can.coords(fruit):
        depopFruit()
        popFruit()

    fen.after(225, move)


def check(event):
    global deplacement
    global score
    global ancienDeplacement
    if score != 0:
        if ancienDeplacement == "s" and event.char in ["s", "q", "d"]:
            deplacement = event.char
        elif ancienDeplacement == "d" and event.char in ["s", "z", "d"]:
            deplacement = event.char
        elif ancienDeplacement == "z" and event.char in ["q", "z", "d"]:
            deplacement = event.char
        elif ancienDeplacement == "q" and event.char in ["q", "s", "z"]:
            deplacement = event.char
    elif score == 0 and event.char in ["z", "s", "d", "q"]:
        deplacement = event.char


def end():
    global score
    lose = Toplevel(fen)
    msgPerdu = Label(lose, text="Vous avez perdu.\nVotre score était de : " + str(score), width=50)
    msgPerdu.config(font=(30))
    msgPerdu.pack()


def start():
    bouttonLancer.destroy()
    fen.geometry('700x600')
    popFruit()


def popFruit():
    global fruit
    global listeQueue
    listeCoord = []
    for i in listeQueue:
        listeCoord.append(can.coords(i))
    x1 = randint(0, 9) * 50
    y1 = randint(0, 9) * 50
    fruit = can.create_oval(x1, y1, x1 + 50, y1 + 50, fill="red")

    while can.coords(fruit) in listeCoord or can.coords(fruit) == can.coords(teteSerpent):
        depopFruit()
        x1 = randint(0, 9) * 50
        y1 = randint(0, 9) * 50
        fruit = can.create_oval = (x1, y1, x1 + 50, y1 + 50)


def depopFruit():
    can.delete(fruit)


fen = Tk()
fen.title("Snake")
score = 0
x, y = 200, 200
taille = 500
deplacement = "z"
compteur = 0
compteurQueue = 0
listeQueue = []
listeCompteur = []
can = Canvas(fen, width=taille, height=taille, highlightthickness=3, highlightbackground="black", bg='#CEC5C5')
can.pack(side=TOP, padx=20, pady=20)
tailleFen = [str(taille + 200), "x", str(taille + 200)]
fen.geometry(''.join(tailleFen))
fen.resizable(False, False)
bouttonLancer = Button(fen, text='Lancer', command=lambda: [start(), move()], bg='black', fg='green', width=30,
                       height=15)
bouttonLancer.pack(padx=5, pady=10)
teteSerpent = can.create_oval(x, y, x + 50, y + 50, fill="#70F047", outline="red", width=2)
registre = [can.coords(teteSerpent)]
labelScore = Label(fen, text="Score : " + str(score))
labelScore.pack()
fen.mainloop()
