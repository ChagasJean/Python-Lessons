# Crie um programa que faça o computador jogar Pedra Papel Tesoura com você.

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
0 - PEDRA
1 - PAPEL
2 - TESOURA''')

jogador = int(input('Qual será sua jogada? '))

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[computador]))

if computador == 0:  # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 1:  # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 2:  # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida!')
