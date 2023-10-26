#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#EX: Ana Maria de Souza
#Primeiro = Ana
#Ultimo = Souza

name = str(input('Qual seu nome? '))

names = name.split()
primeiro = names[0]
ultimo = names[-1]

print('Primeiro nome: {}'.format(primeiro))
print('Ultimo nome: {}'.format(ultimo))