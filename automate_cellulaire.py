from tkinter import *
import random
import time

#Definition des variables

tk=Tk()
largeur_matrice=30 #le nombre de cellule en largeur
hauteur_matrice=30 #le nombre de cellule en hauteur
cote=15 #la taille d'un coté d'une cellule
vivant=1 #Definition de l'etat vivant
mort=0 #Definition de l'etat mort
vitesse=100 #vitesse de changement du tableau

#Création des différentes matrices
cell = [[0 for row in range(largeur_matrice)] for col in range(hauteur_matrice)] 
etat = [[mort for row in range(largeur_matrice)] for col in range(hauteur_matrice)]
temps = [[mort for row in range(largeur_matrice)] for col in range(hauteur_matrice)]

def tableau():
	calculer()#On calcule l'etat des cellules
	dessiner()#On modifie la fenentre avec les nouvaux etats
	
	tk.after(vitesse,tableau)#On recommence pour rechanger la fenetre à une vitesse donnée

def init():
	for y in range(hauteur_matrice):
		for x in range(largeur_matrice):
			#On met l'etat de toute les cellule en morte et leur prochain etat aussi
			temps[y][x]=mort
			cell[y][x]=Canvas(tk,width=cote,height=cote,bg='white')#On cree une cellule
			cell[y][x].grid(column=x,row=y)#On place la cellule à ses coordonnées
			etat[y][x]=mort 


	
	nb_vivant_debut=largeur_matrice*hauteur_matrice//4#On initialise le nombre de cellule vivantes au début de la partie
	liste_viv_debut=[]# On crée une liste avec toutes les cellules vivantes

	while len(liste_viv_debut)<=nb_vivant_debut:#tant qu'on a pas le nombre de cellule vivante voulue:
		cellule_vivante= random.randint(0,largeur_matrice*hauteur_matrice-1)#On choisit une cellule aléatoirement
		x=cellule_vivante%largeur_matrice#On prend la coordoné x de la cellule
		y=cellule_vivante//largeur_matrice#On prend la coordonnée y de la cellule
		if not cellule_vivante in liste_viv_debut: #On vérifie que la cellule n'a pas déjà été choisi
			liste_viv_debut.append(cellule_vivante)#On ajoute la cellule à celles choisies pour etre vivante

			etat[y][x]=vivant #On definit son etat à vivant
			cell[y][x].configure(bg='black')#On mets la cellule en noir


def calculer():
	for y in range(hauteur_matrice):
		for x in range(largeur_matrice):			
			nb_vivant=0#On initialise le nombre de cellules voisines vivantes à 9
			x_haut,y_haut=x,(y-1)%hauteur_matrice#coordonnés voisin du haut
			x_bas,y_bas=x,(y+1)%hauteur_matrice#coordonnée voisin du bas
			x_droite,y_droite=(x+1)%largeur_matrice,y#coordonnée du voisin de droite
			x_gauche,y_gauche=(x-1)%largeur_matrice,y#coordonnée du voisin de gauche
			diag_hg_x,diag_hg_y=(x-1)%largeur_matrice,(y-1)%hauteur_matrice#coordonnée du voisin à la diagonale gauche en haut
			diag_hd_x,diag_hd_y=(x+1)%largeur_matrice,(y-1)%hauteur_matrice#coordonnée du voisin à la diagonale droite en haut
			diag_bg_x,diag_bg_y=(x-1)%largeur_matrice,(y+1)%hauteur_matrice#coordonnée du voisin à la diagonale gauche en bas
			diag_bd_x,diag_bd_y=(x+1)%largeur_matrice,(y+1)%hauteur_matrice#coordonnées du voisin à la diagonale droite en bas
		
			
			#On vérifie si les voisins sont vivants et on ajoute 1 au nombre de voisin vivants
			if etat[y_haut][x_haut]==1:
				nb_vivant+=1
			if etat[y_bas][x_bas]==1:
				nb_vivant+=1
			if etat[y_gauche][x_gauche]==1:
				nb_vivant+=1
			if etat[y_droite][x_droite]==1:
				nb_vivant+=1
			if etat[diag_bd_y][diag_bd_x]==1:
				nb_vivant+=1
			if etat[diag_bg_y][diag_bg_x]==1:
				nb_vivant+=1
			if etat[diag_hd_y][diag_hd_x]==1:
				nb_vivant+=1
			if etat[diag_hg_y][diag_hg_x]==1:
				nb_vivant+=1

			if etat[y][x]==vivant:
				if nb_vivant==2 or nb_vivant==3:# si la cellule est vivante et qu'elle a au 2 ou 3 voisins vivants elle reste en vie
					temps[y][x]=vivant
				else:
					temps[y][x]=mort
			else:
				if nb_vivant==3: #si la cellule est morte mais qu'elle a exactement 3 voisins elle nait
					temps[y][x]=vivant
	
	for y in range(hauteur_matrice):
		for x in range(largeur_matrice):
			#On attribue à état sa nouvelle valeur
			nouvelle_etat=temps[y][x]
			etat[y][x]=nouvelle_etat

def dessiner():
	for y in range(hauteur_matrice):
		for x in range(largeur_matrice):
			#On change la couleur des cellules en fonction des changements d'etats
			if etat[y][x]==vivant:
				cell[y][x].configure(bg='black')
			else:
				cell[y][x].configure(bg='white')




init()
tk.after(vitesse,tableau)		
tk.mainloop()