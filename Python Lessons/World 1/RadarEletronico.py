#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custas R$7.00 por cada km acima do limite.

maxi = 80
multa = float(7)


v1 = float(input("Qual foi a velocidade do carro? "))

if v1 > maxi:
    print("Você foi multado, pague a multa!")
    alem = v1 - 80
    pagarM = alem * multa
    print("A multa é de R${:.2f}".format(pagarM))
else:
    print("Você não foi multado.")