
import turtle
t = turtle.Turtle()

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.backward(100)
# t.right(45)


def imprimer_escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


# imprimer_escalier(30, 10)

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


carre(100)


def carres(taille_depart, nb):
    for i in range(0, nb):
        t.forward(taille_depart + 10)
        t.left(90)


carres(100, 5)


turtle.done()

