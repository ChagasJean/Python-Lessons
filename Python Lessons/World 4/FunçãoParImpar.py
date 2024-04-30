def par_impar(x):
    if x % 2 == 0:
        return "Par"
    elif x % 2 != 0:
        return "Impar"
    else:
        print("Valor inválido!")
    
    
num = int(input("Digite um número: "))

print(par_impar(num))