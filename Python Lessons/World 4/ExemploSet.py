# EXEMPLO DE USO DE SETS

letras = set()
while True:
    letra = input("Digite uma letra: ").lower()
    letras.add(letra)
    
    if "l" in letras:
        print("FAZ O L!")
        break
    print(letras)