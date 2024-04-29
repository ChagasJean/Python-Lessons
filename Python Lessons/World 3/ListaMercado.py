compras = [] # Lista criada

while True: 

    index = range(len(compras)) # Criação do index para enumerarmos os itens
    
    opcao = input("Escolha uma opção \n[I]nserir - [A]pagar - [L]istar - [E]ncerrar: ").capitalize()
    
    if opcao == "E":
        break
    
    elif opcao == "L":
        if not compras: # Caso a lista esteja vazia, ira mostrar o print de baixo
            print("Lista vazia!")
        else:
            for index in index: # Lista enumerada
                print(index, compras[index])
                
    elif opcao == "I":
        
        inserir = input("Insira o nome do produto: ").capitalize()
        
        compras.append(inserir) # Aqui ele adiciona itens ao final da lista
        
    elif opcao == "A":
        if not compras: # Caso a lista esteja vazia, vai mostrar o print à baixo
            print("Não há o que apagar!")
        else:
            for index in index:
                print(index, compras[index]) # Para mostrar a lista enumerada, para que fique mais fácil de visualizar
                
            index_str = input("Escolha um index para apagar: ") # Aqui puxamos o input como str para que fique mais fácil utilizar o int
            
            try: # Nesse try, o index_srt que é uma string, foi transformado em um número inteiro, para que seja possível localizar como um index
                index = int(index_str)
                del compras[index] # Utilizando o index, agora como inteiro, a função del apaga o index selecionado
                print("Produto apagado!")
            except ValueError: # Caso o usuário escreva algo que não seja um index, o programa vai mostrar a mensagem de erro à baixo
                print("Digite um número de index!")
            except IndexError: # Caso o usuário escreva um index que não existe na lista, o programa vai mostrar a mensagem de erro à baixo
                print("Index não localizado!")
    else:
        print("Entrada inválida! Insira novamente.")

