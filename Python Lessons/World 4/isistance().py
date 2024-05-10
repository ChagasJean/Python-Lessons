lista = [
    "A", 1, 1.1, True, [0,1,2], (1,2), {0,1}, {"Nome:": "Luiz"},
]

# Fazendo a verificação de cada função:
for item in lista:
    if isinstance(item, str):
        print("")
        print("STR:")
        print("Antes do metódo:", item, isinstance(item, str))
        print("Depois do metódo:", item.lower(), isinstance(item, str))
    elif isinstance(item, float):
        print("")
        print("FLOAT:")
        print("Antes do metódo:", item, isinstance(item, float))
        print("Depois do metódo:", item + 1, isinstance(item, float))
    elif isinstance(item, bool):
        print("")
        print("BOOL:")
        print("Antes do metódo:", item, isinstance(item, bool))
        print("Depois do metódo:", item is False, isinstance(item, bool))
    elif isinstance(item, list):
        print("")
        print("LIST:")
        print("Antes do metódo:", item, isinstance(item, list))
        item.append(3)
        print("Depois do metódo:", item, isinstance(item,list))
    elif isinstance(item, tuple):
        print("")
        print("TUPLE:")
        print(item, isinstance(item, tuple))
    elif isinstance(item, set):
        print("")
        print("SET:")
        print("Antes do metódo:", item, isinstance(item, set))
        item.add(2)
        print("Depois do metódo:", item, isinstance(item, set))
    elif isinstance(item, dict):
        print("")
        print("DICT:")
        print(item, isinstance(item, dict))
        
        
        
        
    
