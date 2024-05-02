# Manipulando chaves e valores em dicionários
# Index são apenas tipos númericos, enquanto as chaves podem ser todos os imutáveis

pessoa = {
}

#Dict   Chave     Valor
# pessoa["nome"] = "Luiz"

# print(pessoa)
# print(pessoa["nome"])

# Dicionário e chave dinamica

nome = "nome"
sobrenome = "sobrenome"

pessoa[nome] = "Luiz"
pessoa[sobrenome] = "Miranda"

print(pessoa[nome])

pessoa[nome] = "Jean"

del pessoa[sobrenome]
print(pessoa)
print(pessoa["nome"])

if pessoa.get("sobrenome") is None:
    print("Não existe")
else:
    print(pessoa["sobrenome"])
