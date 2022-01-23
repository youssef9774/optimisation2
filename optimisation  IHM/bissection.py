def fonction(x):

    #x**5-5*x(**3) - 20*x+5
    return (x**5)-5*(x**3) - 20*x+5


a = 0
b = 1
e= 0.001
print()
print('************************** Bissection ********************************')
print('a = 0')
print('b = 1')
print('e= 0.001')
print('***********************')
while b-a>10**(-10) and b-a > e:
    
        resultat= (a+b)/2
        if fonction(a)*fonction(resultat)<=0:
            b=resultat
        else:
            a=resultat
        
        print('***********')
        print('intervale entre a=',a,'et  b=',b)
       
        print('resultat = ',resultat)
        print('***********')
   

def af1():
    print('******  variable *****')
    print('a = 0')
    print('b = 1')
    print('e= 0.001')
    print('***********************')
    print('************************** FIN Bissection ********************************')
    print()

af1()

