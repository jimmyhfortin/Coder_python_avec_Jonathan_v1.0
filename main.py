"""mon
    premier
        programme"""


def afficher_informations_personne(nom, age):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age + 1) + " ans")
    if age <= 10:
        print("vous etes enfant")
    elif age == 17:
        print("Vous etes mineur")
    elif age == 18:
        print("Felicitation vous etes majeur")
    elif age >= 60:
        print("Vous etes senior")
    elif age >= 18:
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + "Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR: Vosu devez rentrer un nombre pour l'age")
    return age_int

# Demander le nom


nom1 = demander_nom()
nom2 = demander_nom()

# demander l"age
age1 = demander_age(nom1)
age2 = demander_age(nom2)
# Afficher les informations
# afficher_informations_personne

# Afficher les resultats
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)


