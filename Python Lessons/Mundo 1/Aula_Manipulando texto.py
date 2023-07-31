#PARTE TEÓRICA

#frase = "Olá mundo, bem vindo todos"
'''Cada caracter dentro da string "frase" vai ocupar um espaço de memória dentro da memória do computador, os espaços também contam. Cada caracter é numerado com um indíce.'''

#TÉCNICA DE FATIAMENTO
#Consiste em pegar o indice espéficio dentro da variável "frase", por exemplo: frase[9] = ",", pois o caracter "," está no espaço Nº9 de memória da variavel "frase".
#Existe outros exemplos também, como por exemplo: frase[9:13], ele vai pegar a letra que estiver no espaço Nº9 e vai até o antecessor do número Nº13, que seria a letra "m", então eles escreveria ", be".
#Outro exemplo também é: frase[9:15:2], onde 9 é o caracter ",", o 15 seria "v" e o número 2 representa que o programa deve pular de 2 em 2, ou seja, ficaria ",b".
#Mais um exemplo é: frase[:5], não colocar nada antes dos : é porque o fatiamento vai começar do indice 0, que é a primeira letra da variável "frase", a letra "O".
#Um inverso desse exemplo seria: frase[5:], onde ele vai pegar a letra no indice 5, que é a letra "u" e iria até o final da string, formando "undo, bem vindo todos".
#frase[9::3] ele vai pegar o indice 9, ir até o final e pulando de 3 em 3, que ficaria ",evdto".

frase = 'Olá mundo, bem vindo todos'
frase2 = '   Olá todos  '

#=========================TESTE DE CÓDIGO=============================================
#print(frase[9])
#print(frase[9:13])
#print(frase[9:13:2])
#print(frase[:5])
#print(frase[5:])
#print(frase[9::3])
#=========================TESTE DE CÓDIGO=============================================

#TÉCNICA DE ANÁLISE
#O comando len(frase) é usado para mostrar o comprimento da string e quantos espaços ela ocupa na memória, no caso da varíavel "frase", seriam 26 espaços.
#O comando frase.count('') é usado para contar quantos caracteres específicos existem dentro da string, um exemplo: frase.count('o') = 4, dentro da string "frase", existem 4 letras "o". LEMBRANDO QUE O COMANDO CONTOU APENAS AS LETRAS "o" NO MINUSCULO, PARA PEDIR EM MAISCULO, EU PRECISO ESCREVER A LETRA "o" EM MAISCULA DENTRO DO COMANDO.
#Um outro exemplo desse mesmo comando, é misturar ele com o fatiamento, por exemplo: frase.count('o', 0, 13), ele vai contar quantas letras "o" tem do indice 0 até o indice 13, lembrando que o último indice indicado é sempre excluido, sendo assim, o número de letras "o" dentro desse limite seriam: 1.
#O comando frase.find('') é usado para encontrar um conjunto de caracteres dentro da string e apontar em qual espaço da memória esse conjunto começou, por exemplo: frase.find('mun') = 1 e começou no espaço 4.
#Se dentro desse comando eu colocar algo que não existe, como por exemplo "Jean", o comando vai retornar valor -1, pois o que eu pedi não existe dentro dessa string.
#Usando o operador "in", o programa vai retornar um valor booleano (true ou false) se o que você pediu exister dentro da string, por exemplo: 'mundo' in frase = true.

#=========================TESTE DE CÓDIGO=============================================
#print(len(frase))
#print(frase.count('o'))
#print(frase.count('o', 0, 13))
#print(frase.find('mun'))
#print(frase.find('Jean'))
#print('mundo' in frase)
#print('Jean' in frase)
#=========================TESTE DE CÓDIGO=============================================

#TÉCNICA DE TRANSFORMAÇÃO
#O comando frase.replace('', '') é usado para trocar a string selecionada por outra, por exemplo: frase.replace('mundo', 'planeta'), ele vai procurar a string mundo e substituir pela string planeta.
#O comando frase.upper() é usado para transformar caracteres minúsculos em maiúsculo, mantendo os que já estão, por exemplo: frase.upper() = "OLÁ MUNDO, BEM VINDO TODOS"
#O comando frase.lower() vai ser o total inverso do comando upper, trocando o que está maiúsculo para minúsculo, por exemplo: frase.lower() = "olá mundo, bem vindo todos"
#O comando frase.capitalize() vai trocar todos os caracteres, menos o primeiro, para minusculo.
#Parecido com o comando capitalize, o comando frase.title() vai contar a quantidade de frases dentro da string e colocar os primeiros caracteres de cada uma em maiúsculo, por exemplo: frase.title() = "Olá Mundo, Bem Vindo Todos"
#Vamos mudar a string para poder ensinar esse próximo comando, então vamos usar a string "   Olá todos  ". O comando frase.strip() elimina os espaços que existem no começo e no fim, ficando "Olá todos". LEMBRANDO QUE ELE NÃO ELIMINA OS ESPAÇOS QUE EXISTEM ENTRE AS FRASES, APENAS OS ESPAÇOS NO COMEÇO E NO FIM.
#Parecido com o comando anterior, o comando frase.rstrip() vai eliminar os espaço que estão no final, na direita, ficando: "   Olá todos".
#Sendo o inverso do de cima, o frase.lstrip() elimina os espaços do inicio na esquerda, ficando: "Olá todos  ".

#=========================TESTE DE CÓDIGO=============================================
#print(frase.replace('mundo', 'planeta'))
#print(frase.upper())
#print(frase.lower())
#print(frase.capitalize())
#print(frase.title())
#print(frase2.strip())
#print(frase2.rstrip())
#print(frase2.lstrip())
#=========================TESTE DE CÓDIGO=============================================

#TÉCNICA DE DIVISÃO DE STRINGS
#O comando frase.split() vai ler os espaços que existem dentro da string e separar cada palavra, colocando elas dentro de uma lista, cada palavra separada é numerada e tratada como strings diferentes, usando aquela primeira string, ficaria "Olá", "mundo," "bem", "vindo", "todos", respectivamente, 1, 2, 3, 4, 5.

#=========================TESTE DE CÓDIGO=============================================
#print(frase.split())
#=========================TESTE DE CÓDIGO=============================================

#TÉCNICA DE JUNÇÃO DE STRINGS
#Usando o comando '-'.join(frase) ele vai pegar os splits númerados do comando anterior e juntar elas, colocando um "-" entre cada palavra, ficando: "Olá mundo, bem vindo todos".

#=========================TESTE DE CÓDIGO=============================================
#print('-'.join(frase))
#=========================TESTE DE CÓDIGO=============================================

#UM EXTRA: se eu quiser escrever textos longos e enormes e não quiser ficar colocando print por linha, eu posso usar """ """, o que facilita muito as coisas, por exemplo
#print("""DHASJKDHAJKSDHASJKDHJKASHDJKASHDJKASHDKJASHDKJASHDJKASDHASJKDHASJKDHASJKDHASKJDHASJKDHASJKDHAJSKDHKJASDHKJASHDJKASHDAJKSHDKJASHDSJKADHASJKDHASKJDHASJKDHJASKDHASKJDHASJKDHASJKDHAJKSDHSAJKHDJASKDHJASKDHASJKDHAKJSDHASJKDHASKJHDJKASHDJKSAHDJKSAHDJKASHDJKASHDJKASHDJKSAHDJKASHDJKASHDJKASHDJKAS""")

