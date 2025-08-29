import sys
import random
from datetime import datetime

def maxMinVetSuperOtim(vet):
    numComp = 0

    tamVet = len(vet)

    if ((tamVet & 1) > 0): # verifica se a quantidade de elementos do vetor e impar 
        vet.append(vet[tamVet-1]) # se for adiciona o penultimo elemento como ultimo para ficar par 

    tamVet = len(vet)
    
    if (vet[0] > vet[1]):    
        min = 1
        max = 0
    else:
        min = 0
        max = 1

    # i = 2 
    # while i < tamVet-1:
    #     numComp += 3
    #     prox = i + 1
    #     if (vet[prox] > vet[i]):
    #         if(vet[prox] > max):
    #             max = vet[prox]
    #         if (vet[i] < min):
    #             min = vet[i]
    #     else:
    #         if (vet[prox] < min):
    #             min = vet[prox]
    #         if (vet[i] > max):
    #             max = vet[i]
    #     i +=2
    
    # return min, numComp, max
    
    # comeca do 3 pois como ja foram verificados o v[0] e v[1] assim , i = 3 e ant = i - 1 = 2  
    i = 3
    while i < tamVet:
        numComp += 1
        ant = i-1
        if (vet[ant] > vet[i]): 
            numComp += 1
            if (vet[ant] > vet[max]): 
                max = ant
            numComp += 1
            if (vet[i] < vet[min]): 
                min = i 
        else: 
            numComp += 1
            if (vet[ant] < vet[min]):
                min = ant
            numComp += 1    
            if (vet[i] > vet[max]): 
                max = i 
        i += 2
    return max, numComp, min



if __name__ == '__main__':

    v = []

    random.seed(int(datetime.now().strftime('%H%M%S')))
    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    else:
        n = 20
    for i in range(n):
        v.append(random.randint(0, 1000))

    posMax, qnt_cmpout, posMin = maxMinVetSuperOtim(v)

    print(f"[ ", end = '')
    for i in range(n-1):

        if (i == posMax) or (i == posMin):
            print(f"\033[1;92m", end = '')
        else:
            print(f"\033[1;37m", end = '')

        print(f"{v[i]}\033[1;37m, ", end = '') 

    if (n-1 == posMax):
        print(f"\033[1;92m", end = '')
    else:
        print(f"\033[1;37m", end = '')

    print(f"{v[n-1]}\033[1;37m]") 

    print(f"Maior elemento da sequencia = {v[posMax]}, Menor elemento da sequencia = {v[posMin]} quantidade de comparações = {qnt_cmpout}")
