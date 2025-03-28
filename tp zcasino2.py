from random import randrange
from math import ceil
import os
argent = 1000
print("Bienvenue au Zcasino.")
z=True
while z ==True:
    numero=randrange(50)
    print("Vous avez",argent,"$")
    nom_entré = input("Entrez le nombre sur lequel vous misez.")
    c=True
    while c==True:
        try:
            nom_entré=int(nom_entré)
            nom_entré =ceil(nom_entré)
            c=False
        except :
            print(erreur)
            nom_entré = input("Entrez le nombre sur lequel vous misez.")

        if nom_entré <0:
            print("Vous avez entré un nombre négatif")
            nom_entré = input("Entrez le nombre sur lequel vous misez.")
        elif nom_entré > 49:
            print("Vous avez entré un nombre supérieur à 49.")
            nom_entré = input("Entrez le nombre sur lequel vous misez.")

    mise=input("Entrez la somme d'argent que vous misez")
    b=True
    while b==True:
        try:
            mise = int(mise)
            mise=ceil(mise)
            b=False
        except:
            print(erreur)
            mise=input("Entrez la somme d'argent que vous misez")

    d = True
    while d == True:
        if mise > argent:
            print("Vous misé plus d'argent que vous avez")
            mise=input("Entrez la somme que vous misez")
            mise =int(mise)
            mise=ceil(mise)
        elif mise<0:
            print("Vous avez rentré un nombre négatif.")
            mise=input("Entrez la somme que vous misez")
            mise =int(mise)
            mise=ceil(mise)
        else:
            d=False
    argent=argent-mise
    if nom_entré == numero:
        argent = mise*3+argent
        argent=ceil(argent)
        print("Vous avez gagné , votre argent monte donc à ",argent,"$")
    elif nom_entré%2 == 0 and numero%2 == 0 or nom_entré%2 != 0 and numero%2 != 0:
        gain = mise*50/100
        gain=ceil(gain)
        argent = gain+argent
        argent=ceil(argent)
        print("Vous êtes tombé sur la bonne couleur vous avez donc",argent,"$")
    else:
        print("Vous avez perdu , votre argent descend donc à",argent,"$")

    if argent ==0:
        print("Vous n'avez plus d'argent")
        print("Fin de la partie.")
        z=False
        os.system("pause")
        break
    reponse =input("Souhaitez vous continuer Si oui entrez 'oui'Si non entrez 'non'")
    if reponse =="non" or reponse=="Non" or reponse=="NON":
        z=False
    elif reponse=="oui" or reponse=="Oui" or reponse=="OUI":
        continue
    else:
        z=False
    
    
    
    
