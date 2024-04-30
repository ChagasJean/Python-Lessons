CPF = "74682489070"
digitos = CPF[:9]
contador = 10

result = 0
for digito in digitos:
    result += int(digito) * contador
    contador -= 1

valor = result * 10
valorMod = valor % 11

if valorMod > 9:
    print("O primeiro dígito do CPF é 0")
else:
    print("O primeiro dígito do CPF é {}".format(valorMod))
    
    
    