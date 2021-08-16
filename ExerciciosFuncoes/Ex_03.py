#%% 03 - soma 3 argumentos

"""
Faça um programa, com uma função que necessite de três argumentos, e que 
forneça a soma desses três argumentos.
"""

def soma_abc(a, b, c):
    return a + b + c

def inserir_int_sistema():
    while True:
        try:
            numero = float(input("Informe um numero: "))
            return numero
        except ValueError:
            print('Informe um numero inteiro')

print(soma_abc(inserir_int_sistema(),inserir_int_sistema(),inserir_int_sistema()))
