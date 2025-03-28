from fonctions import*
from données import *
import os 
c=True
while c==True:
    print("Bienvenue dans la partie de pendu.")
    nom=input('Entrez votre pseudo')
    mot_choisi=random.choice(list_mots)
    mot_choisi=str(mot_choisi)
    cripte=criptage(mot_choisi)
    print(cripte)
    décripte=décriptage(cripte,mot_choisi,nb_chance)
    e=décripte
    compte_score=compte_score(e,nb_chance)
    print("Le score est de ",compte_score)
    inscri_score=inscri_score(dico_score,compte_score,nom)
    print(inscri_score)
    r=str(input('Entrez "q" si vous voulez quittez le jeu et "c" pour continuer'))
    if r.lower() == "q":
        c=False
    elif r.lower()=="c":
        continue
    else:
        os.system("pause")
