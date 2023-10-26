# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS.
# EX: APOS A SOPA; A SACADA DA CASA; A TORRE DA DERROTA; O LOBO AMA BOLO; ANOTARAM A DATA DA MARATONA;


frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('NÃO TEMOS UM PALÍNDROMO!')
