# TRY, EXCEPT, ELSE E FINALLY PARA TRATATAR EXCEÇOES

def DivZero(a, b):
    c = a / b

def FaltaV(a, b):
    c = a + b
    
def Indice(string):
    print(string[1000])
    
try:
    a = 18
#    b = 2
    c = a + b
except NameError as nome:
    print("MSG:", nome)
    print("Nome:", nome.__class__.__name__)
    
print("")
    
try:
    DivZero(18, 0)
except ZeroDivisionError as zero:
    print("MSG:", zero)
    print("Nome:", zero.__class__.__name__)

print("")

try:
    FaltaV(1)
except TypeError as tipo:
    print("MSG:", tipo)
    print("Nome:", tipo.__class__.__name__)
    
print("")
    
try:
    Indice("Luiz")
except IndexError as index:
    print("MSG:", index)
    print("Nome:", index.__class__.__name__)
