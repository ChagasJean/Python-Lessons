frase = "Olha a bola, bola que rola"

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""

while i < len(frase):
    letra_atual = frase[1]
    qtd_atual = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
        
    i += 1
    
print("A letra que apareceu mais vezes foi {}, que apareceu {}x".format(letra_apareceu_mais_vezes, qtd_apareceu_mais_vezes))