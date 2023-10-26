# Refaça o desafio dos triângulos do último mundo, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais.
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.

#AQUI É PARA REGISTRAR OS VALORES NAS VARIÁVEIS 'A', 'B' E 'C'.
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

#AQUI É A ESTRUTURA PARA DESCOBRIR SE É POSSIVEL FORMAR UM TRIANGULO E DESCOBRIR SEU TIPO.
if a + 6 > c and a + c > b and b + c > a:
    print("É possível forma um triângulo com essas retas.")
    if a == b == c:
        print("É um triângulo Equilátero!")
    elif a == b or a == c or b == c:
        print("É um triângulo Isósceles!")
    else:
        print("É um triângulo Escaleno")
else:
    print("Não é possível formar um triângulo com essas retas.")