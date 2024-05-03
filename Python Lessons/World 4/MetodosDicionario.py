# MÉTODOS UTÉIS DOS DICIONÁRIOS
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorn uma cópia rasa
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o ultimo item adicionado
# update - atualiza um dicionário com outro

'''
pessoa = {
    "nome": "Luiz",
    "sobrenome": "Miranda",
}
'''

# pessoa.setdefault("idade", 10)
# print(pessoa["idade"])

# print(len(pessoa)) Retorna o número de chaves do dicionário
# print(list(pessoa.keys())) Retorna o nome das chaves
# print(list(pessoa.values())) Retorna os valores das chaves
# print(list(pessoa.items())) Retorna a chave e seu valor

#import copy

'''
d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0,1,2],
}
'''

# d2 = d1.copy() Essa é uma cópia rasa, onde não é possível copiar em subcamadas do dicionário
# d2 = copy.deepcopy(d1) # Essa é uma cópia profunda, que acessa subcamadas

# d2["c1"] = 10
# d2["l1"][1] = 9999

# print(d1)
# print(d2)

p1 = {
    "nome": "Luiz",
    "sobrenome": "Miranda",
}

# print(p1.get("nome", "Não existe")) Mostra a chave especificada, caso ela não exista, vai mostrar uma valor None ou outro atribuido

# nome = p1.pop("nome") Retira a chave selecionada de dentro do dicionário
# print(nome)
# print(p1)

# ultima_chave = p1.popitem() Retira a última chave do dicionário
# print(ultima_chave)
# print(p1)

'''
p1.update({
    "nome": "Roberto",
    "idade": 32,
})
'''

tupla = (("nome", "roberto"), ("idade", 32))
p1.update(tupla)
print(p1)



