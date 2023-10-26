#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0.50 por KM para viagens até 200KM e R$0.45 para viagens mais longas.

dist = int(input("Quantos KM de distância tem a viagem? "))

if dist <= 200:
    preco = dist * 0.50
    print("O valor da viagem é de R${}".format(preco))
else:
    preco2 = dist * 0.45
    print("O valor da viagem é de R${}".format(preco2))
