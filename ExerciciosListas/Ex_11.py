#%% 11 - 3 vetores

"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""


def input_elementos(n):
    vetor = []
    for i in range(n): 
        elemento = (input(f'Insira {n} elementos, elemento {i+1}: '))
        vetor.append(elemento)
    return vetor

elementos, vetores = 10, 3
dc_vetores = {}       
for i in range(vetores): dc_vetores[i] = input_elementos(elementos)

vetor_merge = []
for item in range(elementos):
    for key in range(vetores): vetor_merge.append(dc_vetores[key][item])
