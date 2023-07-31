#Para importar bibliotecas completar sem ser espéfico, usamos o comando:
#import (números) -> Ele vai importar todos os números que tiver dentro dessa biblioteca.

#Para importa algo espéfico de dentro dessas bibliotecas, fazemos outro comando:
#from (números) import (3) -> Ele vai importar apenas o número 3 de dentro da biblioteca.

#A biblioteca math importa operadores matemáticos para o programa. (Essa já vem como padrão).
#A funcionalidade ceil faz arredondamentos para cima, enquanto a funcionaldade floor faz arredondamentos para baixo.
#A funcionalidade trunc elimina os números após a vírgula.
#A funcionalidade pow funciona similar ao operador ** (Potenciação).
#A funcionalidade sqrt é usada para calcular a raiz quadrada de um número.
#A funcionalidade factorial é usada para calcular o fatorial de um número.

#ABAIXO UM CÓDIGO USADO PARA ESTUDAR IMPORTAÇÕES. AQUI EU IMPORTO 3 FUNCIONALIDADES, UMA DE RAIZ QUADRADA, OUTRA DE ARREDONDAR NÚMEROS PARA CIMA E OUTRO PARA ELIMINAR NÚMEROS APÓS A VÍRGULA.

'''from math import sqrt, floor, trunc

num = int(input("Digite um número: "))
raiz = sqrt(num)

print("A raiz quadrada de {} é {:.2f}".format(num, floor(raiz)))'''

#ABAIXO É UM CÓDIGO USADO PARA ESTUDAR IMPORTAÇÕES. AQUI EU IMPORTO A BIBLIOTECA RANDOM, ONDE A MÁQUINA ESCOLHE OS NÚMEROS PARA MIM.

'''import random

num = random.random() #Assim você gera um número float entre 0 e 1
print(num)

num2 = random.randint(1, 10) #Assim gera um número inteiro entre 1 e 10 (Ou um número a sua escolha).
print(num2)'''


