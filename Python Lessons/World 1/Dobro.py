#Crie um algoritmo que leia o número e mostre seu sobro, triplo e raiz quadrada

n1 = float(input("Escreva um número: "))

dob = n1 * 2
trip = n1 * 3
rq = n1 ** (1/2)

print("O dobro de {} é {}".format(n1, dob))
print('O triplo de {} é {}'.format(n1, trip))
print("A raiz quadrada de {} é {:.2f}".format(n1, rq))

