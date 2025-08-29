# #######################################
# Módulo que determina a posição do 
# maior elemento de um vetor de inteiros
# utilizando funções.
# #######################################

import sys
import random
from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
def maxVet(vet):
    
    max = vet[0]
    posM = 0
    qnt_cmp = 0

    for i in range(1, len(vet)):
        qnt_cmp += 1
        if (max < vet[i]):
            max = vet[i]
            posM = i
            

    return posM, qnt_cmp

# *******************************************************
# ***                                                 ***
# *******************************************************
# se o programa for executado diretamente da linha de comando ele executa oq está em __name__ == '__main__' 
# caso o programa for chamado via import ele executa oq está fora.
if __name__ == '__main__':

    v = []

    random.seed(int(datetime.now().strftime('%H%M%S')))

    if (len(sys.argv) > 1):  # scape code python color 
        n = int(sys.argv[1]) # caso rode o codigo python3 maxVetor.py 4 ele vai pegar o 4 como argumento e atribuir ele para n 
    else:
        n = 20

    for i in range(n):
        v.append(random.randint(0, 1000))

    posMax, qnt_cmpout = maxVet(v)

    print(f"[ ", end = '')
    for i in range(n-1):

        if (i == posMax):
            print(f"\033[1;92m", end = '')
        else:
            print(f"\033[1;37m", end = '')

        print(f"{v[i]}\033[1;37m, ", end = '') 

    if (n-1 == posMax):
        print(f"\033[1;92m", end = '')
    else:
        print(f"\033[1;37m", end = '')

    print(f"{v[n-1]}\033[1;37m]") 

    print(f"Maior elemento da sequencia = {v[posMax]} quantidade de comparações = {qnt_cmpout}")
