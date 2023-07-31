#Crie um código que converta temperatura em Celsius para Kelvin e Fihrenheit

C = float(input('Qual a temperatura em C? '))

K = C + 273.15
F = ((9 * C)/5) + 32

print('A temperatura de {} Celsius é {} Kelvin e {} Fihrenheit'.format(C, K, F))