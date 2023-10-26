#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

#O CÓDIGO ABAIXO CALCULA A HIPOTENUSA USANDO LÓGICA MATEMÁTICA DO PROPRIO PROGRAMA
'''catOP = float(input('Qual o comprimento do cateto oposto? '))
catAD = float(input('Qual o comprimento do cateto adjacente? '))

hipo = (catOP ** 2 + catAD ** 2) ** (1/2)

print('A hipotenusa é {:.2f}.'.format(hipo))'''

#O CÓDIGO ABAIXO CALCULA A HIPOTENUSA USANDO O MÓDULO HYPOT, QUE FAZ A HIPOTENUSA AUTOMATICAMENTE
catOP = float(input('Qual o comprimento do cateto oposto? '))
catAD = float(input('Qual o comprimento do cateto adjacente? '))

hipo = hypot(catOP, catAD)

print('A hipotenusa mede {:.2f}'.format(hipo))
