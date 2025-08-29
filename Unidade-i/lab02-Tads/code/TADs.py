# #########################################
# Utiliza Tipo Abstrato de Dados (TADs) 
# nativos do Python
# #########################################

import sys

counter  = 100
max = counter

print("counter", type(counter), hex(id(counter)))
print("max", type(max), hex(id(max)))

max = 99
counter  = 1

print("counter", type(counter), hex(id(counter)))
print("max", type(max), hex(id(max)))
