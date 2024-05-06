# Sets - Conjunto em Python
# Em Python, sets são mutáveis, porém aceitam apenas 
# tipos mutáveis como valor interno.


# Criando um sets
# s1 = set() # Vazio
# s1 = {"Luiz", 1, 2, 3} # Com dados


# Sets são eficientes para remover valores duplicados de iteráveis
# ELes não tem indexes
# Eles não garantem ordem
# Eles são iteráveis (for in, not in)

# l1 = [1,2,2,2,2,2,2,3]
# print(l1, type(l1))
# s1 = set(l1)
# print(s1, type(s1))
# l2 = list(s1)
# print(l2, type(l2))
#s1 = {1,2,3}
#for s in s1:
#    print(s)


# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# print(s1)
# s1.add(1)
# print(s1)
# s1.add("Luiz")
# print(s1)
# s1.update(("Valor a ser descartado", 1,2,3,4))
# print(s1)
#s1.clear() # Esse metódo limpa o set inteiro
# s1.discard("Valor a ser descartado")
# print(s1)


# Operadores úteis:
# União (|) união (union) - Une
# Intersecção (&) (intersection) -> Itens presentes em ambos
# Diferença (-) Itens presentes apenas no set da esquerda
# Diferença simétrica (^) -> Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
print(s1, s2)
s3 = s1 | s2
print("União:",s3)
s3 = s1 & s2
print("Intersecção:",s3)
s3 = s1 - s2
print("Diferença:",s3)
s3 = s1 ^ s2
print("Diferença simétrica:",s3)











