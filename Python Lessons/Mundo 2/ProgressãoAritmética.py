# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA P.A. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

primeiro_termo = int(input("Digite o primeiro termo da P.A.: "))
razao = int(input("Digite a razão da P.A.: "))

print("Os 10 primeiros termos da P.A. são:")
for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo, end=" ")
