# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES QUE SÃO MULTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.

s = 0

for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print('A soma de todos os números ímpares e múltiplos de três dentro do intervalo de 1 e 500 é de: {}'.format(s))
