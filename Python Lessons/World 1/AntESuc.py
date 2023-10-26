#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor

n1 = int(input("Escreve uma número: "))

ant = n1 - 1
suc = n1 + 1

print('O sucessor de {} é {}'.format(n1, suc))
print('O antecessor de {} é {}'.format(n1, ant))