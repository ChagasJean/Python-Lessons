# ESCOPOS GLOBAIS E LOCAIS
# E. GLOBAIS = TODO O CÓDIGO É ALCANCÁVEL
# E. LOCAIS = APENAS NOMES DO MESMO LOCAL PODEM SER ALCANÇADOS, POR EXEMPLO, EM UMA FUNÇÃO

x = 1 # Esse x está no escopo global do código

def escopoLocal():
    #global x
    x = 10 # Esse x está no escopo local do código
    
    def outra_funcao(): # A função escopoLocal não pode acessar y, pois está dentro de outra função
        #global x
        x = 11
        y = 2 
        print(x, y)
        
    outra_funcao()
    #print(x)
    
print(x)
escopoLocal()
print(x) # Mesmo após executar a função, o x desse print continua sendo o do escopo global







