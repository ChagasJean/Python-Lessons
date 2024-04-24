'''
Lista em Python
Tipo List - Mutável
Suporta vários valores de qualquer Tipo
Conhecimentos reutilizáveis
Métodos úteis: append, insert, pop, del, clear, extend, +
    append -> Adiciona um item ao final da lista
    insert -> Adiciona um item no índice escolhido
    pop    -> Remova do final ou do índice escolhido
    del    -> Apaga um índice 
    clear  -> Limpa a lista
    extend -> Estende a lista
    +      -> Concatena listas

Create Read Update   Delete
Criar  Ler  Alterar  Apagar = lista[i] (CRUD)
'''

#             0    1     2       3    4                                  #
    lista = [132, True, "Luiz", 1.2, []] # Aqui utilizamos o CREATE      #  
    print(lista)                                                         # 
                                                                         # ESSE BLOCO EXPLICA O BÁSICO DAS LISTAS    
    lista[2] = "Maria" # Aqui utilizamos o UPDATE                        # FALANDO SOBRE O CREATE, READ, UPDATE E DELETE      
    print(lista) # Aqui utilizamos o READ                                #
    del lista[4] # Aqui utilizamos o DELETE                              #
    print(lista)                                                         #


lista2 = [10, 20, 30, 40] 
print(lista2)
lista2.append(50) # Esse comando é pra adicionar um novo valor no final da lista
print(lista2)
lista2.pop() # Esse comando remova o último elemento da lista
print(lista2)
lista2.insert(0, 5)
print(lista2)
lista2.clear() # Esse comando limpa a lista e remove todos os valores dentro dela
print(lista2)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b # Aqui as duas listas foram concatenadas utilizando o operandor '+'
print(lista_c)



