# CONDIÇÕES ANINHADAS: É QUANDO SE COLOCA MAIS DE UM CONDIÇÃO DENTRO DE UMA UNICA ESTRUTURA

# EXEMPLO EM CÓDIGO
# carro.siga()
# if carro.esquerda():
#   carro.siga()
#   carro.direita()
#   carro.siga()
#   carro.direita()
#   carro.esquerda()
#   carro.siga()
#   carro.direita()
#   carro.siga()
# elif carro.direita():
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
# else:
#   carro.siga()
# carro.pare()

name = str(input('Qual seu nome? '))

if name == 'Jean':
    print("Olá")
elif name == 'Lucas' or name == 'Marcos' or name == 'Maria':
    print('Seu nome é bem popular!')
elif name in 'Ana Cláudia Jéssica Juliana':
    print("Um belo nome feminino")
else:
    print("Seu nome é bem normal!")

print("Tenha um bom dia, {}!".format(name))
