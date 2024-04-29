nomes = ["Maria", "Luiz", "Jean"]

nome1, nome2, nome3 = nomes

while True:

    escolha = input("Escolha um nome [Nome1 - Nome2 - Nome3]: ").capitalize()
    
    if escolha == "Nome1":
        print(nome1)
    elif escolha == "Nome2":
        print(nome2)
    elif escolha == "Nome3":
        print(nome3)
    elif escolha == "0":
        print("Saiu!")
        break
    else:
        print("Valor inválido!")