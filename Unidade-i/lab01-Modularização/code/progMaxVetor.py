# #######################################
# Programa que determina a posição do 
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

    for i in range(1, len(vet)):

        if (max < vet[i]):
            max = vet[i]
            posM = i

    return posM

# *******************************************************
# ***                                                 ***
# *******************************************************

v = [];

random.seed(int(datetime.now().strftime('%H%M%S')))

if (len(sys.argv) > 1):
    n = int(sys.argv[1])
else:
    n = 20

for i in range(n):
    v.append(random.randint(0, 1000))

posMax = maxVet(v)

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

print(f"Maior elemento da sequencia = {v[posMax]}")
