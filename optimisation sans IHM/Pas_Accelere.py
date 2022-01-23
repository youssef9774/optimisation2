print()
print('**************************PAS ACCELEREE********************************')
print('\n\n*** Trouvez l’optimum de la fonction suivante en utilisant les méthodes demandées ***')

print ('la fonction : 𝑓 = 𝑥⁵ − 5𝑥³ − 20𝑥 + 5')
print ('Recherche avec un pas fixe accéléré')
#Pas_accelere
def x(i,first_position,x1):
    if i>0:
        return x1+(i-1)*first_position
    else:
        return x1+(i+1)*first_position


def fonction(i,first_position,x1):
    return x(i,first_position,x1)**5-5*(x(i,first_position,x1)**3) - 20*x(i,first_position,x1)+5
    

def pas_acc():
    x1=0.0
    first_position=0.05
    s=first_position
    i=1
    if fonction(2,first_position,x1)<fonction(1,first_position,x1):
        while fonction(i+1,first_position,x1)<fonction(i,first_position,x1): 
            i+=1
            first_position *= 2
        x1=x(i-1,first_position,x1)
        x2=x(i,first_position,x1)
        i1 = i
        if i1 != 0 : 
           print('Notre solution trouver c est X =',i1)
        else:
            print()
    if fonction(2,first_position,x1)>fonction(1,first_position,x1):
        while fonction(i+1,first_position,x1)>fonction(i,first_position,x1):
            i-=1
            first_position *= 2
        x1=x(i-1,first_position,x1)
        x2=x(i,first_position,x1)
        i1 = i
        if i1 != 0 : 
            print('Notre solution trouver c est X =',i1)
        else:
            print()
    elif fonction(2,first_position,x1)==fonction(3,first_position,x1):
        x1=x(1,first_position,x1)
        x2=x(2,first_position,x1)
    elif fonction(2,first_position,x1)>fonction(1,first_position,x1):
        x1=x(-2,first_position,x1)
        x2=x(2,first_position,x1)
        if i1 != 0 : 
            print('Notre solution trouver c est X =',i1)
        else:
            print()
    return i1,x1,x2,first_position

def aff_acc(pas_acc):
    r=pas_acc()
    i=r[0]
    x1=r[1]
    x2=r[2]   
    first_position=r[3]
    s=first_position
    



    print(" resultat in ",x1)
    print('xi',' = x1 + s' , first_position)
    print('Valeur de s=' ,s)
    print('fi =f(xi)' ,fonction(i+1,first_position,x1))
    print()
    print('************************** FIN PAS ACCELEREE********************************')
    print()
aff_acc(pas_acc)







