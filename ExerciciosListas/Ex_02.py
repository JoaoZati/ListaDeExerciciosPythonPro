#%% Exemplo 2 Renzo Ex-02

"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na 
ordem inversa.
"""

vetor = []
for _ in range(5):
    numero = float(input('Digite um numero: '))
    vetor.append(numero)
    
vetor.reverse()
print(f'{vetor}')
