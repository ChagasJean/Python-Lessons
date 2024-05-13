# RAISE - LANÇANDO EXCEÇÕES (ERRORS)

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError("Não é possível dividir por 0.")
    return True
    
def deve_ser_numero(n):
    if not isinstance(n, (float, int)):
        raise TypeError(
            f"{n} deve ser um número int ou float"
        )
    return True
       
def divisao(n, d):
    deve_ser_numero(n)
    deve_ser_numero(d)
    nao_aceito_zero(d)
    return n / d

print(divisao(8,2))
