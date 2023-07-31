#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 1 dolar = 3.27 reais

n1 = float(input('Quanto tem na sua carteira? '))

dol = n1 * 3.27

print('Na sua carteira tem R$ {:.2f}'.format(n1))
print('Com essa quantida você pode comprar U$ {:.2f}'.format(dol))