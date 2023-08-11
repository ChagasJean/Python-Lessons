# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
'''
-> A MÉDIA DE IDADE DO GRUPO.
-> QUAL É O NOME DO HOMEM MAIS VELHO.
-> QUANTAS MULHERES TÊM MENOS DE 20 ANOS.
'''

si = 0
mi = 0
mh = 0
nv = ''
totm = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    si += idade

    if p == 1 and sexo in "Mm":
        mh = idade
        nv = nome
    if sexo in 'Mm' and idade > mh:
        mh = idade
        nv = nome
    if sexo in 'Ff' and idade > 20:
        totm += 1

mi = si / 4
print('A média da idade do grupo é de {} anos'.format(mi))
print('O homem mais velho tem {} anos e se chama {}'.format(mh, nv))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm))
