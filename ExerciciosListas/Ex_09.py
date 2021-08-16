#%% 09 - Quadrado dos Elementos

"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e 
mostre a soma dos quadrados dos elementos do vetor.
"""

import numpy as np

def input_numero_int(menssagem):
    while True:
        try:
            num = int(input(menssagem))
            return num
        except ValueError:
            print('Favor inseir um numero inteiro')

def input_vetor_int(tamanho, menssagem):
    vetor = []
    for i in range(tamanho):
        numero = input_numero_int(menssagem + f'{i+1}: ')
        vetor.append(numero)
    return vetor

vetor = input_vetor_int(10, 'Insira 10 numeros, numero ')

for i in range(len(vetor)): vetor[i] *= vetor[i]
soma = 0
for i in vetor: soma += i     

print(f'A soma dos quadrados do vetor é: {soma}')
