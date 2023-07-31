#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça pro usúario tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usúario venceu ou perdeu.

from time import sleep
from random import randint

n1 = randint(0, 5)

n2 = int(input("Qual número eu pensei? "))
print("Pensando...")
sleep(2.5)

if n2 == n1:
    print("Você acertou!")
else:
    print("Você errou!")
    print("O número certo era {}".format(n1))

