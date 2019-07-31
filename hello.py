#-*-coding: utf-8 -*-
#print "Hello world"
#print("Outra mensagem")#comentario
#print("Olá Mundo")
#operacoes matematicas
#print(2+2) #soma
#print(2**3) #esponenciação
#print(10%3) #resto

#variáveis
#mensagem="Olá mundo"
#print(mensagem)

#Operadores relacionais
#x=3
#y=2
#print(x==y)

#operadores lógicos
#soma = x+y
#print(x==y and x==soma)
#print(x==y or x==soma)

#Operadores Condicionais

x = 1
y = 10

if x>y:
    print("x é maior que y")
if y>x:
    print("y é maior que x")


if x>y:
    print("x é maior que y")
else:
    print("y é maior que x")

a = 1
b = 2


#if a == b:
#    print("a é igual a b")
#elif a < b:
#    print("a é menor que b")
#else:
#    print("y é maior que x")


#x = 1

#while x < 10: 
#    print(x)
#    x = x+4


lista1 = [1,2,3,4,5]
lista2 = ["ola", "mundo","!"]
lista3 = [0,"ola","biscoito", "bolacha",9.99, True]

for i in lista3:
    print(i)

#função range
for i in range(10):
    print(i)

for i in range(10,20): #vai imprimir de 10 à 19
    print(i)

for i in range(10,20,2): #vai imprimir de 10 à 18 só que de 2 em 2
    print(i)