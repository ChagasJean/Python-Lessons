""" import os

x = 0

def duplicar(x):
    return x * 2

def triplicar(x):
    return x * 3

def quadruplicar(x):
    return x * 4

while True:

    print("Bem-vindo!")

    num = int(input("Digite um valor: "))
        

    opcao = input("Escolha uma opção:\n[D]uplicar\n[T]riplicar\n[Q]uadruplicar\n").capitalize()
    
    if opcao == "D":
        os.system("cls")
        resultado = duplicar(num)
        print(f"Duplicar o número {num} resulta em {resultado}")


    elif opcao == "T":
        os.system("cls")
        resultado = triplicar(num)
        print(f"Triplicar o número {num} resulta em {resultado}")

    elif opcao == "Q":
        os.system("cls")
        resultado = quadruplicar(num)
        print(f"Quadruplicar o número {num} resulta em {resultado}")
        

    else: 
        print("Opção inválida!")
        break
 """

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

