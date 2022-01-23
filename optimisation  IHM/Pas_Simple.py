print()
print('**************************PAS SIMPLE********************************')
print('\n\n*** Trouvez l’optimum de la fonction suivante en utilisant les méthodes demandées ***')

print ('la fonction : 𝑓 = 𝑥⁵ − 5𝑥³ − 20𝑥 + 5')
print ('Recherche avec un pas fixe Simple')

s=0.05
first_position=0.0

def x(i):
    if i>0:
        return first_position+(i-1)*s
    else:
        return first_position+(i+1)*s


def fonction(i):
    return x(i)**5-5*(x(i)**3) - 20*x(i)+5

def s_fixe():
    i=1
    if fonction(2)<fonction(1) :
        while fonction(i+1)<fonction(i): 
            i+=1
        x1=x(i-1)
        x2=x(i)
        
    elif fonction(2)>fonction(1):
        while fonction(i+1)>fonction(i):
            i-=1
        x1=x(i-1)
        x2=x(i)

       
    
    elif fonction(2)>fonction(1):
        x1=x(-2)
        x2=x(2)
        
    
    elif fonction(2)==fonction(3):
        x1=x(1)
        x2=x(2)
        
    return i,x1,x2

def aff_simple(fonction, s_fixe):
    r=s_fixe()
    i=r[0]
    
    x2=r[2] 
    

    print()
    print('fi',fonction(i+1),'>','fi−1 ',fonction(i),'---> Vrai') 
    
    print('********************')
    print('la valeur de s', s)
    print('fi = f(xi)',fonction(i))
    print('x',i,'= x1 + s =',x2)
    print('Notre solution trouver c est ','i =',i)

    print()
    print('************************** FIN PAS SIMPLE ********************************')
    print()


aff_simple(fonction, s_fixe)
                 
             

    