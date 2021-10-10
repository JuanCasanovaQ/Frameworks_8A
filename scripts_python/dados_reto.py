from math import factorial
import os
from random import randint

#Functions
def dices() :
    status = True
    meta=0
    pares = 0

    while status :     #while status ==> while status == True
        os.system("clear")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("D1: ", dice1)
        print("D2: ", dice2)
        meta = meta + dice1 +dice2
        print(meta)
        if meta >= 100 :
                status = False
                print("::: Meta alcanzada. El lanzamiento ha finalizado :::")
        if dice1 == dice2 :
            pares = pares + 1
            if pares == 2 :
                status = False
                print("::: Dos pares consecutivos. El lanzamiento ha finalizado :::")
        else :
            pares = 0
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")
#Main
dices()