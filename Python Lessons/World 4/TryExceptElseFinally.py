# TRY, EXCEPT, ELSE E FINALLY

# Esse tipo de try sempre vai executar todos os comandos dentro dele, até o finally
try:
    print("Começo do código.")
    a = 8 / 0
except ZeroDivisionError:
    print("Divisão por 0.")
finally:
    print("Final do código.")
