#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo: '))

sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print('O ângulo {:.2f} tem valor de seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang, sen, coss, tang))