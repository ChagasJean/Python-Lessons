# REFAÇA O DESAFIO DA TABUADA, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTLIZANDO O LAÇO FOR.

print('-=-' * 5)
print('    TABUADA')
print('-=-' * 5)

n = int(input('Digite um valor: '))

for num in range(1, 11):
    m = n * num
    print('{} x {}: {}'.format(n, num, m))
