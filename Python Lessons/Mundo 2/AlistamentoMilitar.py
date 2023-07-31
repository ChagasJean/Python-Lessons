# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai ser alistar ao serviço militar.
# Se é a hora dele se alistar.
# Se já passou o tempo do alistamento
# Seu programa também deverá mostrar o campo que falta ou que passou do prazo.

# AQUI É PARA IMPORTAR A FUNÇÃO DATE, PARA SABER O ANO DO SEU SISTEMA DO COMPUTADOR.
from datetime import date

# AQUI É PARA REGISTRAR O NASCIMENTO DO USUÁRIO.
ano = int(input('Qual o ano do seu nascimento? '))

# AQUI É PARA A VARIÁVEL 'ANO2' TER SEU VALOR CLASSIFICADO COMO O ANO DO SISTEMA DO SEU COMPUTADOR.
ano2 = date.today().year

# AQUI É O CALCULO PARA DESCOBRIR A IDADE DO USUÁRIO.
calculo = ano2 - ano

print("Quem nasceu em {} tem {} anos em {}".format(ano, calculo, ano2))

# AQUI É A ESTRUTURA PARA FAZER AS MENSAGENS CERTAS APARECEREM NA TELA.
if calculo == 18:
    print('Você tem que se alistar agora!')
elif calculo < 18:
    saldo = 18 - calculo
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano3 = ano2 + saldo
    print('Seu alistamento será em {}'.format(ano3))
elif calculo > 18:
    saldo = calculo - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano3 = ano2 - saldo
    print('Seu alistamento foi em {}'.format(ano3))
