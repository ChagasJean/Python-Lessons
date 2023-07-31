#Faça um programa que leia algo escrito pelo teclado e retorne todas as informações possíveis sobre ele.

a = input('Escreva algo: ')

print(type(a))
print('É alfabético? ', a.isalpha())
print('É númerico? ', a.isnumeric())
print('Tudo maiscula? ', a.isupper())
print('Tudo minuscula? ', a.islower())
print('Tem espaços? ', a.isspace())