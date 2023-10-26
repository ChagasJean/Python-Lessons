# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

# AQUI É PARA IMPORTAR A FUNÇÃO DATE, PARA SABER O ANO DO SEU SISTEMA DO COMPUTADOR.
from datetime import date

# AQUI É PARA REGISTRAR O NASCIMENTO DO USUÁRIO.
ano = int(input('Qual o ano do seu nascimento? '))

# AQUI É PARA A VARIÁVEL 'ANO2' TER SEU VALOR CLASSIFICADO COMO O ANO DO SEU COMPUTADOR.
ano2 = date.today().year

# AQUI É O CALCULO PARA DESCOBRIR A IDADE DO USUÁRIO.
calculo = ano2 - ano
print('O atleta tem {} anos'.format(calculo))

# AQUI É A ESTRUTURA PARA DEFINIR AS CATEGORIAS.
if calculo <= 9:
    print("Sua categoria é: MIRIM")
elif calculo >= 10 and calculo <= 14:
    print("Sua categoria é: INFANTIL")
elif calculo >= 15 and calculo <= 19:
    print("Sua categoria é: JUNIOR")
elif calculo == 20:
    print("Sua categoria é: SÊNIOR")
else:
    print("Sua categoria é: MASTER")
