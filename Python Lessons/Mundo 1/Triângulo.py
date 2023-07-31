#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário de elas podem ou não formar um triângulo.

a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if a + 6 > c and a + c > b and b + c > a:
    print("É possível forma um triângulo com essas retas.")
else:
    print("Não é possível forma um triângulo com essas retas.")