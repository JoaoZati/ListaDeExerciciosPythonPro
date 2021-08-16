#%% 08 - Idade e Altura

"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada 
informação no seu respectivo vetor. Imprima a idade e a altura na ordem 
inversa a ordem lida.
"""

import numpy as np

def input_numero_float(menssagem):
    while True:
        try:
            num = float(input(menssagem))
            if num < 0: 
                print('Inserir valores maiores que 0') 
                continue
            return num
        except ValueError:
            print('Favor inseir um numero')

def input_vetor_floats_2(tamanho, menssagem1, menssagem2):
    vetor1, vetor2 = [], []
    for i in range(tamanho):
        numero1 = input_numero_float(menssagem1 + f'{i+1}: ')
        vetor1.append(numero1)
        numero2 = input_numero_float(menssagem2 + f'{i+1}: ')
        vetor2.append(numero2)
    return vetor1, vetor2

vetor_idade, vetor_altura = input_vetor_floats_2(5, 'Insira as idades, Idade Pessoa ', 
                                               'Insira as alturas, Altura Pessoa ')

vetor_idade_reverse = list(reversed(vetor_idade))
vetor_altura_reverse = list(reversed(vetor_altura))

print(f'''Alturas: {vetor_altura_reverse}
Idades: {vetor_idade_reverse}''')
