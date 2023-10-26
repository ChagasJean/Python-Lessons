#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

n1 = float(input('Qual seu salário? '))

nvn1 = (1 + (15 / 100)) * n1

print("Seu novo sálario é de R$ {}".format(nvn1))