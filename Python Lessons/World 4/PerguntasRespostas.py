perguntas = [
    {
        "Pergunta": "Quando é 2+2?",
        "Opções": [4, 22, 6, 10],
        "Resposta": 4,
    },
    {
        "Pergunta": "Quando é 5x5?",  
        "Opções": [5, 10, 25, 55],
        "Resposta": 25,
    },
    {
        "Pergunta": "Quando é 10/2?", 
        "Opções": [12, 8, 20, 5],
        "Resposta": 5,
    },
]

qtd_acertou = 0
for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    print()
    
    opcoes = pergunta["Opções"]
    for i, opcao in enumerate(opcoes):
        print(f"{i})", opcao)
    print()
    
    escolha = input("Escolha uma opção: ")
    
    escolha_int = None
    acertou = False
    qtd_opcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)
        
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta["Resposta"]:
                acertou = True
    
    print()      
    if acertou:
        qtd_acertou += 1
        print("Acertou :D")
    else:
        print("Errou D:")
    
    print()
    
if qtd_acertou == 1:
    print("Meu deus, você só acertou", qtd_acertou, "de", len(perguntas), "perguntas.")
elif qtd_acertou == 2:
    print("Bem na média você em. Acertou", qtd_acertou, "de", len(perguntas), "perguntas.")
elif qtd_acertou == 3:
    print("PARABÉNS, ACERTOU TODAS AS", len(perguntas), "PERGUNTAS.")
else:
    print("Mano, voce errou todas... Eram só", len(perguntas), "perguntas...")














