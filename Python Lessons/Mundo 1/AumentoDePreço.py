#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n1 = float(input('Qual o preço do produto? '))

nvn1 = (1 - (5 / 100)) * n1

print('Com 5 porcento de desconto, o novo valor é de R$ {}'.format(nvn1))