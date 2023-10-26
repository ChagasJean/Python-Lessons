#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a ultima vez.

frase = str(input('Escreva uma pequena frase: '))

print('A quantidade de letras "A": {}'.format(frase.count('A')))
print('A quantidade de letras "a": {}'.format(frase.count('a, á')))
print('A letra "a" aparece pela primeira vez em: {}'.format(frase.find('a')))
print('A letra "a" aparece pela ultima vez em: {}'.format(frase.rfind('a')))
