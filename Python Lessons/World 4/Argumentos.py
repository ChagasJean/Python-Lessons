def conta(x, y, z):
    # Definição
    print(f"{x=} y={y} z={z}", "|", f"x / y * z = {x/y*z:.2f}")
    
conta(1,2,6)
conta(2,1,6) # A ordem em que os argumentos forem colocados, altera os valores da função
conta(y=6, z=6, x=2) # Fazemos assim para que possamos colocar os valores na ordem que quisermos
conta(2,4,6)




