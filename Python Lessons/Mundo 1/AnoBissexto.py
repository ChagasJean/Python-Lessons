#Faça um programa que leia um ano qualquer e mostre se ele e bissexto.

from datetime import date

ano = int(input("Digite um ano: "))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")
