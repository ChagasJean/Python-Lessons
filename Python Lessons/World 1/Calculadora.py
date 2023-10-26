n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
s = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
divin = n1 // n2
mod = n1 % n2

print("A soma de {} e {} é {}".format(n1, n2, s))
print("A subtração de {} e {} é {}".format(n1, n2, sub))
print("A multiplicação de {} e {} é {}".format(n1, n2, mult))
print("A divisão de {} e {} é {}".format(n1, n2, div))
print("A potência de {} e {} é {}".format(n1, n2, pot))
print("A divisão inteira de {} e {} é {}".format(n1, n2, divin))
print("O resto da divisão de {} e {} é {}".format(n1, n2, mod))