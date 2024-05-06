# FUNÇÃO LAMBDA
# A função lambda é uma função como qualquer outra em python.
# Porém, são funções anônimas que contém apenas uma linha.
# Ou seja, tudo deve ser contido dentro de uma única expressão

lista = [
    {"nome": "Luiz", "sobrenome": "Miranda"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Daniel", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]

# def ordena_nome(item):
#    return item["nome"]
    
# lista.sort(key=ordena_nome) Aqui seria um exemplo sem o lambda

def exibir(lista):
    for item in lista:
        print(item)


l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])

exibir(l1)
print("-"*40)
exibir(l2)










