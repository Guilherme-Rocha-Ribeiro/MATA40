import sys
import random
from datetime import datetime

def min_maxVet2(vet):
    
    max = vet[len(vet)-1]
    posMax = 1
    min = vet[0]
    qnt_cmp = 0
    posMin = 0

    for i in range(1, len(vet)):
        qnt_cmp += 1  
        if (max < vet[i]):
            max = vet[i]
            posMax = i
        else:
            qnt_cmp += 1
            if (min > vet[i]):
                min = vet[i]
                posMin = i

    return posMax, qnt_cmp, posMin


if __name__ == '__main__':

    v = []

    random.seed(int(datetime.now().strftime('%H%M%S')))
    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    else:
        n = 20
    for i in range(n):
        v.append(random.randint(0, 1000))

    posMax, qnt_cmpout, posMin = min_maxVet2(v)

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

    
