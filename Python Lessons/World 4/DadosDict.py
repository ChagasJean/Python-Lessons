# Dados Dict - Estrutura de dados do tipo chave e valor
# Chaves podem ser consideradas como "indices" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.
# Dicionarios podem ficar dentro de outros dicionários
# Para criar dicionarios, podem usar as {} ou a classe dict
# Imutáveis: str, int, float, bool, tuple, etc.
# Mutáveis: list, dict

#pessoa = dict(nome= "Luiz", sobrenome="Miranda") # Forma menos usada 

import os

pessoa = { # Aqui a gente cria o dicionário
    "Nome:": "Luiz",
    "Sobrenome:": "Miranda",
    "Idade:": "18",
    "Altura:": 1.80,
    "Endereços:": [
        {"rua": "tal tal", "numero": 123},
        {"rua": "lero lero", "numero": 456},
    ]
}

# print(pessoa["nome"]) # Crtl + K + C para comentar tudo de uma vez
# print(pessoa["sobrenome"])

for chave in pessoa:
    print(chave, pessoa[chave])