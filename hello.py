#-*-coding: utf-8 -*-
a = "Juliana"
b = "Gonçalves"
concatenar = a + " "+ b + "\n"
print(concatenar)

tamanho = len(concatenar)
print(tamanho)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])

print(concatenar[0:5]) #imprime de 0 à 4

#imprime tudo em minusculo
print(concatenar.lower())
print(concatenar.upper())
print(concatenar.strip()) #remove a linha depois da concatenação

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split(" ")
print(minha_lista)

#Busca em substrings, pedaço de uma string
busca = minha_string.find("rei")
print(busca)
print(minha_string[busca:]) #imprime a partir de rei, se não encontrar retorna -1

minha_string.replace("rei", "rainha") #não funciona
minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)