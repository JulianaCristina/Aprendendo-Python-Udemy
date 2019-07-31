#--coding: utf-8 --

lista = [50, 20, 10, 40, 30, 60]

lista.sort() #esse metodo altera lista que já existe

lista = sorted(lista) #cria uma nova lista
lista.sort(reverse=True) #decrescente
lista.reverse() #inverte a lista, torna o primeiro elemento o ultimo
print(lista)