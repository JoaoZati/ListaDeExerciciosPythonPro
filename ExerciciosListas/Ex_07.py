#%% 07 - Leia programa com 5 numeros

"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, 
a multiplicação e os números.
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

vetor = input_vetor_int(5, 'Insira 5 vetores, vetor ')
array_vetor = np.array(vetor)
soma = array_vetor.sum()
multiplicacao = array_vetor.cumprod()[-1]

print(f"""
A soma dos vetores é de: {soma}
A Multiplicação é de: {multiplicacao}
E os vetores são: {array_vetor}
""")
