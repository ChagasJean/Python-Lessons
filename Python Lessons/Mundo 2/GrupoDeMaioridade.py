# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JA SÃO MAIORES.

from datetime import date

anoA = date.today().year
MaI = 0
MeI = 0

for i in range(7):
    nasc = int(input('Digite o ano de nascimento da pessoa: '))
    idade = anoA - nasc

    if idade < 18:
        MeI += 1
    else:
        MaI += 1

print('Quantidade de maiores de idade: {}'.format(MaI))
print('Quantidade de menores de idade: {}'.format(MeI))
