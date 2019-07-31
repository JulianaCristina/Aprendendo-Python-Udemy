#--coding: utf-8 --

# números aleatórios

import random
random.seed(1) #força ele a retornar sempre o msm número, no caso, a segunda posição
#numero = random.randint(0,10)#escolhe um entre 0 e 10
lista = [6,45,9]
numero = random.choice(lista) #escolhe um número aleatório dentre os números da lista
print(numero)