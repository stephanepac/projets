import random
mot="barbara"
def compte_score(nb_tour,tour_total):
    score_parti=tour_total-nb_tour
    return score_parti

def choix_mot(mots):
    mot=random.choice(mots)
    return mot

def criptage(mot):
    i=0
    mot_cripter=""
    while i<len(mot):
        mot_cripter+="*"
        i+=1
    return mot_cripter
mot_cripter=criptage(mot)
mot_cripter=str(mot_cripter)
def décriptage(cripter,mot,nb_tour):
    global e
    e=0
    c=0
    t=0
    while t<nb_tour :
        lettre=input("Entrez votre lettre")
        cripter=list(cripter)
        mot=mot.lower()
        lettre=str(lettre)
        lettre=lettre.lower()
        x=mot.find(lettre)
        if x != -1 and lettre !="":
            print(lettre,"est dans le mot")
            n=0
            while n<len(mot):
                if mot[n] == lettre:
                    cripter[n]=lettre
                n+=1
            print(cripter)
        else:
            print("La lettre n'est pas dans le mot")
            print(cripter)
            e+=1
            c+=1
        if cripter==list(mot):
            print("Bravo tu as trouvé")
            t+=nb_tour
            
        if e>=nb_tour:
            print("Vous n'avez plus d'essais")
            t+=nb_tour
    return e


def inscri_score(dic,score,nom):
    dic=dict(dic)
    if (nom in dic):
        x=dic.get(nom)
        e=int(x)
        if e <score:
            dic[nom] = score
    else:
        dic[nom]=score
    return dict(dic)   
dico={"Louis":8}   
if __name__=="__main__":
    print(inscri_score(dico,7,"Louis"))
    

    
