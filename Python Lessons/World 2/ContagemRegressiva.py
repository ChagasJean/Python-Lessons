# FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRASSIVA PARA O ESTOURO DE FOGOS DE ARTIFÍCIO, INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.

from time import sleep

print('-=' * 18)
print('CONTAGEM REGRESSIVA PRO ANO NOVO!!!!')
print('-=' * 18)
sleep(1)


for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('-=' * 10)
print('FELIZ ANO NOVOOO!!!!')
print('-=' * 10)
