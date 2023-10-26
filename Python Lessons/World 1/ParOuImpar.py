#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

n1 = int(input("Escreva um número: "))

if n1 % 2 == 0:
    print("Este número é par!")
else:
    print("Este número é impar!")