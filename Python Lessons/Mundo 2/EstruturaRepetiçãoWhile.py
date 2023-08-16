'''
ESSA AULA VOU TENTAR MANTER MAIS NA PRÁTICA DO QUE SÓ TEXTOS ENORMES COM EXPLICAÇÕES, QUANDO PRECISAR ESCREVER, VAI SER SÓ PARA EXPLICAR O CÓDIGO.

ESSE AQUI É UM CONTADOR UTILIZANDO O LOOP WHILE, PORÉM SO VAI ATÉ 9, PARA IR ATÉ 10, TERIA QUE COLOCAR O 11 NO LUGAR DO 10:
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

ESSE CÓDIGO É PARECIDO COM AQUELE DE FOR PARA GUARDAR NÚMEROS NA MEMÓRIA, MAS O FOR É OBRIGATÓRIO TER UM LIMITE, COM O WHILE TEM COMO QUEBRAR ESSE LIMITE, DA SEGUINTE FORMA:
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

ESSE CÓDIGO É PARA CONFIRMAÇÃO DE SIM OU NÃO:
r = 'S'
while r == 'S':
    r = str(input('Quer continuar? [S/N])).upper()

ESSE AQUI É PARA VERIFICAR SE UM NÚMERO É PAR OU ÍMPAR:
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: ))
    if n % 2 == 0:
        par +=1 
    else:
        impar += 1        
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
'''
