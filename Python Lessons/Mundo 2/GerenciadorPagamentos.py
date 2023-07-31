# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista em dinheiro/cheque: 10% de desconto.
# À vista no cartão: 5% de desconto.
# Em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% juros.

# AQUI É A PARTE DE REGISTRO E O MENU DE OPÇÕES DO CÓDIGO
valor = float(input('Qual o valor do produto que deseja pagar? '))

print("Escolha a opção de pagamento: ")
print("1 - À vista em dinheiro ou cheque.")
print("2 - À vista no cartão.")
print("3 - 2x no cartão.")
print("4 - 3x ou mais no cartão.")

sel = int(input('Escreva o número da opção desejada: '))

# AQUI É ONDE AS CONDIÇÕES SÃO FEITAS PRA SABER O PREÇO DOS DESCONTOS
if sel == 1:
    print('Você escolheu pagar à vista no dinheiro ou cheque.')
    precoN = valor * 0.9
    print("O valor a ser pago é de R${:.2f}".format(precoN))
elif sel == 2:
    print("Você escolheu pagar à vista no cartão.")
    precoN = valor * 0.95
    print("O valor a ser pago é de R${:.2f}".format(precoN))
elif sel == 3:
    print("Você escolheu parcelar a compra em duas vezes no cartão.")
    print("O preço se mantém como R${:.2f}".format(valor))
elif sel == 4:
    print("Você escolheu parcelar a compra em três vezes no cartão.")
    precoN = valor * 1.2
    print("O valor a ser pago é de R${:.2f}".format(precoN))
else:
    print("Opção inválida.")
