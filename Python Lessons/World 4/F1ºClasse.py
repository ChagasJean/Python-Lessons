# HIGHER ORDER FUNCITIONS - FUNÇÕES DE PRIMEIRA CLASSE

def saudacao(msg, nome):
    return f"{msg}, {nome}"

def executar(funcao, *args):
    return funcao(*args)

print(
    executar(saudacao, "Bom dia", "Luiz")    
)