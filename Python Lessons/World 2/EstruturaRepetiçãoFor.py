# LAÇOS DE REPETIÇÃO

# PARA FAZER REPETIÇÕES DE PRINTS COM STRINGS, FAZEMOS DA SEGUINTE FORMA:
# for c in range(0, 6):
#   print('Oi')

# PARA FAZER REPETIÇÕES DE PRINTS COM NÚMEROS, FAZEMOS DA SEGUINTE FORMA:
# for c in range(0, 6):
#    print(c)

# SE QUISERMOS COLOCAR A ORDEM INVERSA, FAZEMOS DA SEGUINTE FORMA:
# for c in range(6, 0, -1):
#    print(c)
# O -1 DIZ QUE ELE VAI TIRAR UMA UNIDADE DO 6 ATÉ CHEGAR NO NÚMERO DESTINADO.

# SE QUISERMOS CONTAR DE 1 A 10, MAS PULANDO DUAS UNIDADES, FAZEMOS DA SEGUINTE FORMA:
# for c in range(0, 10, 2):
#    print(c)
# O 2 DIZ QUE VAMOS PULAR DUAS CASAS DE UNIDADES, A PARTIR DO NÚMERO 0, MAS ELE NÃO CHEGOU ATÉ O 10, ENTÃO A GENTE COLOCA DE OUTRA FORMA:
# for c in range(0, 12, 2):
#    print(c)
# ASSIM O CÓDIGO IMPLEMENTA O 10, QUE ANTES NÃO ESTAVA.

# PODEMOS FAZER TAMBÉM UM SIMPLES CONTADOR QUE LÊ O NÚMERO FINAL A PARTIR DO SEU TECLADO, DA SEGUINTE FORMA:
# n = int(input('Digite um número: '))

# for c in range(0, n+1):
#    print(c)
# FOI NECESSÁRIO COLOCAR O N+1 PARA QUE O CÓDIGO ADICIONE UM NÚMERO A MAIS NO NÚMERO QUE PEDIMOS, PORQUE O PTYHON NÃO CONTA O ÚLTIMO NÚMERO NA HORA DE CONTAR AS CASAS.

# TEM OUTRAS FORMAS DE UTILIZAR O FOR, POR EXEMPLO:
"""
i = int(input('Inicio: '))  # O número inicial da sequência.
f = int(input('Fim: '))  # O último número dessa sequência.
p = int(input('Passo: '))  # Os passos que a sequência deve seguir.

for c in range(i, f+1, p):
    print(c)
print('FIM!')
"""

# OUTRA FORMA É UTILIZAR O FOR PARA DETERMINAR QUANTAS VEZES UM VALOR PODE SER PEDIDO.
'''
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM!')
'''

# TAMBÉM PODEMOS FAZER UM SOMÁTORIO UTILIZANDO DESSA MESMA ESTRUTURA
'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos números recebidos é de {}'.format(s))
'''
