from time import sleep

while True:
    n1 = input("Digite um valor: ")
    n2 = input("Digite um valor: ")
    operador = input("Escolha um operador (+ - / *): ")
    
    n_validos = None
    n1_float = 0
    n2_float = 0
    
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        n_validos = True
    except:
        n_validos = None
        
    if n_validos is None:
        print("Um ou ambos os números são inválidos!")
        continue
    
    operadores_permitidos = "+-/*"
    
    if operador not in operadores_permitidos:
        print("Operador inválido!")
        continue
    
    if len(operador) > 1:
        print("Escolha apenas um operador!")
        continue
    
    if operador == "+":
        res = n1_float + n2_float
        print("Calculando...")
        sleep(1.5)
        print("O resultado é de {}".format(res))
    elif operador == "-":
        res = n1_float - n2_float
        print("Calculando...")
        sleep(1.5)
        print("O resultado é de {}".format(res))
    elif operador == "/":
        res = n1_float / n2_float
        print("Calculando...")
        sleep(1.5)
        print("O resultado é de {}".format(res))
    elif operador == "*":
        res = n1_float * n2_float
        print("Calculando...")
        sleep(1.5)
        print("O resultado é de {}".format(res))
    else:
        print("Você não deveria estar aqui.")
        break
    
    sair = input("Deseja [s]air? ").lower().startswith("s")
    
    if sair is True:
        break