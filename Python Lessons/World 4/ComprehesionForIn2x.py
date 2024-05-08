lista = []
count = 0

# Um for in dentro do outro para criar uma matriz de diferentes tamanhos:
for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)   
]

for num in lista:
    count += 1
    print(f"{count}:",num)