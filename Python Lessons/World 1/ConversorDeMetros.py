#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n1 = float(input('Escreva os metros: '))

cm = n1 * 100
mm = n1 * 1000

print('O valor de {} em centímetros é {} cm'.format(n1, cm))
print('O valor de {} em milímetros é {} mm'.format(n1, mm))

