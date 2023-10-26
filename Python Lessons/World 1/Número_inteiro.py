#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#EX: Digite um número: 6.235
#O número 6.235 tem a parte inteira 6.

from math import trunc

n1 = float(input("Escreva um número qualquer: "))

print("O número {} tem sua parte inteira {}.".format(n1, trunc(n1)))