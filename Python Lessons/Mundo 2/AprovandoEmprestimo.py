# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('-=-' * 6)
print('    EMPRÉSTIMO')
print('-=-' * 6)
# AQUI É PARA DEFINIR OS VALORES DA VARIÁVEIS 'VALOR', 'SALARIO', 'ANOS'.
valor = float(input("Valor da casa: "))
salario = float(input("Salário do comprador: "))
anos = int(input("Quantos anos de financiamento? "))

# AQUI É PARA FAZER A CONVERSÃO DE ANOS PARA MESES.
meses = anos * 12

# AQUI É PARA O CÁLCULO DA PRESTAÇÃO MENSAL DA CASA.
valorM = valor / meses

# AQUI É PRA DESCOBRIR QUAL OS 30% DO SALARIO
n1 = salario * (30 / 100)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(
    valor, anos, valorM))

# AQUI É A ESTRUTURA PARA DEFINIR A APROVAÇÃO OU NÃO DO EMPRESTIMO
if valorM > n1:
    print("O empréstimo foi negado pois a prestação mensal é menor que seu salário.")
else:
    print("O empréstimo foi aprovado.")

print('-=-' * 10)
print('      FIM DO EMPRÉSTIMO')
print('-=-' * 10)
