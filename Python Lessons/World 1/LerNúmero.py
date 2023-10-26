#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#EX: Digite o número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

n = int(input('Escreva um número de 0 até 9999: '))

unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10

print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)
