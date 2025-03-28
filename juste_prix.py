import tkinter as tk
JustePrix=1375
n=6 #nombre essai

def essai():
    global n
    n-=1
    return n
fenetre=tk.Tk()
l1=tk.Label(fenetre,text="Entrez un nombre entre 1000 et 1500")
l1.grid(row=0,column=0)
e=tk.Entry(fenetre)
e.grid(row=1,column=0)
indice=tk.Label(fenetre,text="")
indice.grid(row=2,column=0)
l2=tk.Label(fenetre,text="Il vous reste "+str(n)+" essai")
l2.grid(row=3 ,column=0)
abandon=tk.Button(fenetre,text="Abandonner",command=fenetre.destroy)
abandon.grid(row=4,column=0)
def valide(a):
    global  position
    global n
    nb=int(e.get())
    if nb==JustePrix:
        l2.config(text="Bravo t'as trouvé")
        indice.config(text="")
        n=6
    elif nb<JustePrix and nb>1000:
        l2.config(text="Il vous reste "+str(essai())+" essais")
        indice.config(text="Cherche plus haut")
    elif nb>JustePrix and nb<1500:
        indice.config(text="Cherche plus bas")
        l2.config(text="Il vous reste "+str(essai())+" essais")
    else:
        indice.config(text="Cherche bien un nombre entre 1000 et 1375")

    e.delete(0, len(e.get()))



valider=tk.Button(fenetre,text="Valider")

valider.bind("<Button-1>",valide)
e.bind("<Return>",valide)


valider.grid(row=1,column=1)



fenetre.mainloop()