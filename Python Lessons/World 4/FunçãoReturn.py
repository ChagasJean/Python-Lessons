# RETORNO DE FUNÇÕES (return)

def soma (x,y):
    if x > 10:
        return [10, 20]
    return x+y # Utilizar return, faz com que seja possível atribuir os valores dessa função para variáveis fora dela
    
    
    
    
    
soma1 = soma(2,2) # 2 + 2 = 4
soma2 = soma(3,3) # 3 + 3 = 6
print(soma1)
print(soma2)
print(soma1+soma2) # 4 + 6 = 10
print(soma(11,3))
