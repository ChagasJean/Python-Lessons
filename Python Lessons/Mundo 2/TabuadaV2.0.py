# REFAÇA O DESAFIO DA TABUADA, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTLIZANDO O LAÇO FOR.

n = int(input('Digite um valor: '))

for num in range(1, 11):
    m = n * num
    print('{} * {}: {}'.format(n, num, m))
