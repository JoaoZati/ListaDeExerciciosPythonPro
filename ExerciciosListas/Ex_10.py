#%% 10 - Dois vetores virando um

"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um 
terceiro vetor de 20 elementos, cujos valores deverão ser compostos 
pelos elementos intercalados dos dois outros vetores.
"""

def input_elementos(n):
    vetor = []
    for i in range(n): 
        elemento = (input(f'Insira {n} elementos, elemento {i+1}: '))
        vetor.append(elemento)
    return vetor
        
vetor1 = input_elementos(10)
vetor2 = input_elementos(10)
vetor3 = []
for i in range(len(vetor1)):
    if i % 2 == 0: 
        vetor3.append(vetor1[i])
    else: vetor3.append(vetor2[i])
    
    
print(', '.join([vetor for vetor in vetor3]))
