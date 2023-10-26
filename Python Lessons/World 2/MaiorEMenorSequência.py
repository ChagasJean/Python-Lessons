# FAÇA UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.

maior = float('-inf')
menor = float('inf')

for i in range(5):
    peso = float(input('Digite o peso de uma pessoa (em KG): '))

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print('Maior peso lido: {} KG'.format(maior))
print('Menor peso lido: {} KG'.format(menor))
