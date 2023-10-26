#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

KM = float(input('Quantos KM percorreu o carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

KMpre = KM * 0.15
diaspre = dias * 60

total = KMpre + diaspre

#Também da pra fazer de outra forma:
#total = (dias * 60) + (KM * 0.15)

print('O preço a se pagar é de R${:.2f}'.format(total))