# CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50.

print('ESSE SÃO OS NÚMEROS PARES ENTRE 1 E 50:')

for c in range(0, 52, 2):
    print(c, end=' ')

'''
OUTRA FORMA DE FAZER TAMBÉM É UTILIZANDO, DENTRO DO FOR, UM IF ELSE, DA SEGUINTE FORMA:

print('ESSE SÃO OS NÚMEROS PARES ENTRE 1 E 50:')

for c in range(1, 51):

    if c % 2 == 0:
        print('c', end=' ')

'''
