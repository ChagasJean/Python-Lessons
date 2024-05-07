import pprint

# List comprehension é uma forma rápida para criar listas a partir de iteráveis

# print(list(range(10)))

# lista = []

# for numero in range(10):
#     lista.append(numero)

# lista = [ # É possível colocar for in dentro de listas
#     numero * 2
#     for numero in range(10)
# ] 
# print(lista)    
def p(v):
    pprint.pprint(novos_preços, sort_dicts=False, width=40)
# Mapeamento de dados em lista comprehesion
produtos = [
    {"nome": "p1", "preço": 20,},
    {"nome": "p2", "preço": 10,},    # Aqui está o dicionário original com os nomes e os preços
    {"nome": "p3", "preço": 30,},
]

novos_preços = [
    {**produto, "preço": produto["preço"] * 1.05} # Esse dicionário é para modificar seus preços
    if produto["preço"] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_preços, sep="\n")

novos_preços = [
    {**produto, "preço": produto["preço"] * 1.05} 
    if produto["preço"] > 20 else {**produto}
    for produto in produtos
    if produto["preço"] > 10
]

p(novos_preços)