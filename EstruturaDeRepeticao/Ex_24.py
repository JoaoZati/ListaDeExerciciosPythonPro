#%% 24 - Media de N notas

"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

import numpy as np

while True:
    try:
        n = int(input('Insira o numero de notas para calcular a média: '))
        if n <= 0:
            print('numero precisa ser maior que 0')
            continue
        break
    except ValueError:
        print('Não foi fornecido um numero inteiro')

lista_n = []
numero = 0
while True:
    try:
        num = float(input(f'Insira {n} notas de 0 a 10, nota numero {numero + 1}: '))
        if 10 < num or num < 0:
            print('O valor tem que estar entre 0 a 10')
            continue
        lista_n.append(num)
        numero += 1
        if numero >= n:
            break
    except ValueError:
        print('Deve informar um numero real')
        
numpy_lista = np.array(lista_n)
num_media = numpy_lista.mean()

print(f'A nota aritimética das notas fornecidas é {num_media}')
