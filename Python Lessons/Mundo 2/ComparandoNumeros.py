# Escreva um programa que leia dois números inteiro e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

#AQUI É PARA DEFINIR OS VALORES DA VARIÁVEIS 'N1' E 'N2'.
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

#AQUI É A ESTRUTURA PARA VER SE OS NÚMEROS SÃO MAIORES QUE UM OU OUTRO OU PARA VER SE SÃO IGUAIS.
if n1 > n2:
    print("{} é maior que {}".format(n1, n2))
elif n2 > n1:
    print("{} é maior que {}".format(n2, n1))
elif n1 == n2:
    print("Ambos os números são iguais.")