texto = "Luiz"

for letra in texto:
    print(letra)
    
#EXPLICAÇÃO TÉCNICA DE COMO O FOR IN FUNCIONA
'''
texto = "Luiz" -> Iterável
iteratador = iter(texto) -> iteratador

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break
'''