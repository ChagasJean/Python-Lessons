# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O.

s = 0 # Aqui eu comecei dando o valor de 0 para a soma.

for c in range(6):
    n = int(input('Digite um valor: '))

    if n % 2 == 0: # Aqui eu fiz um if para descobrir apenas os numeros pares dentro dos valores que foram dados.
        s += n

print('A soma dos valores pares é: {}'.format(s)) # Aqui mostra o resultado.
