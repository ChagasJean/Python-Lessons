# DIR, HASATTR E GETATTR 
# HASATTR - CHECA SE EXISTE UM DETERMINADO NOME DE METÓDO
# GETATTR - EXTRAI O METÓDO DE DENTRO DE UMA STRING

string = "Luiz"

# UMA FORMA DE VER OS METÓDOS DISPONÍVEIS CASO O PROGRAMA QUE UTILIZA NÃO MOSTRAR
dir2 = dir(string)
print(dir2)

for item in dir2:
    print(item)
#