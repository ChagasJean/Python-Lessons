#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250.00, calcule um aumento de 10%.
#Para os inferior ou iguais, o aumento é de 15%.

s1 = float(input("Qual o seu salário? "))

if s1 >= 1250:
    novoS1 = s1 * 1.1
    print("Seu novo salário é de R${:.2f}".format(novoS1))
else:
    novoS2 = s1 * 1.15
    print("Seu novo salário é de R${:.2f}".format(novoS2))