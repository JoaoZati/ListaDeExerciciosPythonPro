#%% Exemplo Renzo Ex-01

"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

vetor = []
for _ in range(10):
    numero = float(input('Digite um numero: '))
    vetor.append(numero)
    
print(vetor)
