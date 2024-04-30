# Refatorar: editar o código

def soma(x,y,z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", "|", f"x + y + z = {x+y+z}") 
    else:
        print(f"{x=} {y=}", "|", f"x + y = {x+y}")
    
soma(1,2)
soma(3,5)
soma(3,8,11)
soma(1,2)