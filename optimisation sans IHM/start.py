import bissection
import Pas_Accelere
import Pas_Simple
import Newton_Raphson




def choix():
    k = input('choisissez un num')
    


    if k == '1':
        my_script = Pas_Simple.s_fixe()
        return my_script

    if k == '2':

        my_script2 = Pas_Accelere.pas_acc()
        return my_script2

    if k == '3':
        my_script3 = bissection.af1()
        return my_script3

    if k == '4':
        my_script3 = Newton_Raphson.newtonRaphson()
        return my_script3

if __name__ == "__main__":
    choix()







    


