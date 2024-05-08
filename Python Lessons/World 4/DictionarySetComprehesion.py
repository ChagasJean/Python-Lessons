# DICTIONARY COMPREHESION E SET COMPREHESION

# DICTIONARYS
produtos = {
    "Nome:": "Caneta Azul",
    "Preço:": 2.5,
    "Categoria:": "Escritório",
}

'''   
dc = {
    chave: valor.capitalize()
    if isinstance(valor, str) else valor
    for chave, valor
    in produtos.items()
}
'''

# for chaves in dc.items():
    # print(chaves)
    
    
# SETS
s1 = {i for i in range(1,11)}
print(s1)









