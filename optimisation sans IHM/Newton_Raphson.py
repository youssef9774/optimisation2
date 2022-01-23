# Defining Function
print()
print('************************** Newton Raphson ********************************')
print('\n\n*** Trouvez l’optimum de la fonction suivante en utilisant les méthodes demandées ***')

print ('la fonction : 𝑓 = 𝑥³ − 7𝑥² + 8𝑥 − 3')
def fonction(x):
    return x**3 - 7*(x**2) + 8*x- 9

# Defining derivative of function
def Derivé(x):
    return 3*x**2 - 14*x + 8

# Implementing Newton Raphson Method

def newtonRaphson(x0_initial,e,N):

    print ('La solution pour la fonction : 𝑓 = 𝑥³ − 7𝑥² + 8𝑥 − 3')

    print('\n\n*** Newton Raphson ***')
    
    step = 1
    i = 1
    condition = True
    while condition:
        try:
            if Derivé(x0_initial) == 0.0:
                print('Divide by zero error!')
                break

        except ZeroDivisionError:
             print("try again")
        
        x_suivante = x0_initial - fonction(x0_initial)/Derivé(x0_initial)
        print('X-%d, X= %0.6f -------- fonction(x) = %0.6f' % (step, x_suivante, fonction(x_suivante)))
        x0_initial = x_suivante
        step = step + 1
        
        if step > N:
            i = 0
            break
        
        condition = abs(fonction(x_suivante)) > e
    
    if i==1:
        print('\nRequired root is: %0.8f' % x_suivante)
        print('notre solution c\'est X=',step-1)
    else:
        print('\nil y a encore d iteration essaye de mettre plus de nombre pour N.')


# Input Section
x0_initial = input('Enter point initial X0: ')
e = input('Epsilon ε : ')
N = input('Nombre d iteration maximum N : ')

# Converting x0_initial et e to float
x0_initial = float(x0_initial)
e = float(e)

# Converting N to integer
N = int(N)


# Starting Newton Raphson Method
newtonRaphson(x0_initial,e,N)

print()
print('************************** FIN Newton Raphson ********************************')