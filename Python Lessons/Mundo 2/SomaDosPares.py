# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O.

s = 0  # Aqui eu comecei dando o valor de 0 para a soma.
cont = 0

for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))

    if n % 2 == 0:  # Aqui eu fiz um if para descobrir apenas os numeros pares dentro dos valores que foram dados.
        s += n
        cont += 1
# Aqui mostra o resultado.
print('Você digitou {} número(s) par(es) e a soma foi: {}'.format(cont, s))
