#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas a letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar os espaços)
#Quantos letras tem o primeiro nome

name = str(input('Qual seu nome? '))

primeiro_nome = name.split()[0] #AQUI TIVE QUE FAZER UMA PEQUENA GAMBIARRA PARA SEPARAR A STRING E NA LINHA DE BAIXO FAZER A CONTAGEM
quant = len(primeiro_nome)

print('Tudo em maiúsculo: {}'.format(name.upper())) #AQUI USAMOS UPPER PARA DEIXAR TUDO EM MAIÚSCULO
print('Tudo em minúsculo: {}'.format(name.lower())) #AQUI USAMOS LOWER PARA DEIXAR TUDO EM MINÚSCULO
print('Quantas letras tem o nome?', len(name)-name.count(' ')) #AQUI TIVE QUE FAZER ALGO MAIS TRABALHADO, O QUE ACONTECE AQUI, É QUE PRIMEIRO NÓS LEMOS QUANTOS CARACTERES TEMOS NA STRING INSERIDA E EM SEGUIDA USAMOS O COUNT, PARA CONTAR A QUANTIDADE DE ESPAÇOS QUE TEM, COM ISSO COLOCAMOS O "-" PARA ELE TIRAR OS ESPAÇOS QUE ESTÃO CONTADOS PELO COUNT, RETORNANDO O VALOR DA STRING PARA QUALQUER STRING QUE FOR COLOCADA
print('Quantas letras tem o primeiro nome? {}'.format(quant))