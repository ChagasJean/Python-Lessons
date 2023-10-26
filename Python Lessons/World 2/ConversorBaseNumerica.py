# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# 1 para binário.
# 2 para octal
# 3 para hexadecimal

# CÓDIGO SIMPLES PARA A CRIAÇÃO DE UM PEQUENO MENU DE OPÇÕES
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

selecao = int(input("Escolha a entrada: "))

# UTLIZANDO IF ELIF, AQUI FOI CRIADO CONDIÇÕES PARA QUE AS OPÇÕES FOSSEM ESCOLHIDAS E O RESULTADO OBTIDO
if selecao == 1:
    n1 = int(input('Escreva um número: '))
    print('{} convertido para BINÁRIO é igual a {}'.format(n1, bin(n1)[2:]))
elif selecao == 2:
    n1 = int(input('Escreva um número: '))
    print('{} convertido para OCTAL é igual a {}'.format(n1, oct(n1)[2:]))
elif selecao == 3:
    n1 = int(input('Escreva um número: '))
    print('{} convertido para HEXADECIMAL é igual a {}'.format(
        n1, hex(n1)[2:]))
else:
    print("Entrada inválido")
