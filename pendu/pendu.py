from fonctions import*
from données import *
import os 
c=True
while c==True:
    try:
        print("Bienvenue dans la partie de pendu.")
        nom=input('Entrez votre pseudo')
        mot_choisi=random.choice(list_mots)
        cripte=criptage(mot_choisi)
        print(cripte)
        décripte=décriptage(cripte,mot_choisi,nb_chance)
        e=décripte
        compter_score=compte_score(e,nb_chance)
        print("Le score est de ",compter_score)
        inscrire_score=inscri_score(dico_score,compter_score,nom)
        dico_score=inscrire_score
        print("Les records sont :",inscrire_score)
        r=str(input('Entrez "q" si vous voulez quittez le jeu et "c" pour continuer'))
        if r.lower() == "q":
            c=False
        elif r.lower()=="c":
            continue
        else:
            os.system("pause")
    except:
        print("Erreur !!!")
        print("Veuillez recommencer")
