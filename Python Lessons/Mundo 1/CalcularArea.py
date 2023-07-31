#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2m^2.

larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))

print('A largura da parede é de {} metros e a altura é de {} metros'.format(larg, alt))

a = larg * alt

print('A área dessa parede é de {} metros ao quadrado.'.format(a))

lit = a / 2

print('A quantidade de litros de tinta necessário é de {} litros'.format(lit))