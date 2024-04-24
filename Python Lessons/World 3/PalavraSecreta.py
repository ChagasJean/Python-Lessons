#import os -> biblioteca/módulo usada para utilizar o comando para deixar o terminal limpo sempre o jogador ganhar.

palavra_secreta = "perfume"
letras_acertadas = ""
tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    tentativas += 1
    
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    print("Palavra formada:", palavra_formada)
    
    if palavra_formada == palavra_secreta:
        #os.system("cls") -> Comando usado para limpar o terminal do VSCode no Windows.
        print("PARABÉNS, VOCÊ ADIVINHOU A PALAVRA SECRETA!!!")
        print("A palavra secreta era", palavra_secreta)
        
        if tentativas == 6:
            print("PARABÉNS, FOI UMA VITÓRIA PERFEITA!")
        elif tentativas > 6:
            print("Seu número de tentativas foi de {}".format(tentativas))
        
        break