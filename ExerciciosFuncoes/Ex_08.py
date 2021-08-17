#%% 08 - Quantidade Digitos

"""
Faça uma função que informe a quantidade de dígitos de um determinado 
número inteiro informado.
"""

def inserir_numero_sistema(menssagem):
    while True:
        try:
            numero = int(input(menssagem))
            if numero <= 0:
                print('Informar numero maior igual a 0')
                continue
            return numero
        except ValueError:
            print('Informe um numero inteiro')

def inverter_numerro():
    numero = inserir_numero_sistema('Insira um numero inteiro (0<num): ')
    print(len(str(numero)))

inverter_numerro()
