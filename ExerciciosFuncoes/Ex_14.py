#%% 14 - Quadrado magico

"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e 
colunas, com um número em cada posição e no qual a soma das linhas, 
colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de 
lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados 
mágicos com as características acima. Dica: produza todas as combinações 
possíveis e verifique a soma quando completar cada quadrado. Usar um 
vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""

numeros = list(range(1, 10))


possibilidades = []

for i in range(1, 10):
    possibilidades.append([i])

def adicionar_elemento(possibilidades):
    for i in range(len(possibilidades)):
        for j in range(1, 10):        
            if j not in possibilidades[i]:
                novo = possibilidades[i] + [j]
                possibilidades.append(novo)
            
    maior = len(possibilidades[-1])
    possibilidades = [i for i in possibilidades if len(i) == maior]
    
    return possibilidades

while True:
    possibilidades_0 = possibilidades
    possibilidades = adicionar_elemento(possibilidades)
    if possibilidades_0 == possibilidades: break

def verificar_array_igual(array):
    bool_output = True
    for i in range(1, len(array)):
        if array[i] != array[i-1]: bool_output = False
    return bool_output

bool_soma = True
quadrados_magicos = []
for array_p in possibilidades:
    array_soma = [0]*8
    for j in range(3):
        array_soma[0] += array_p[j]
        array_soma[1] += array_p[j+3]
        array_soma[2] += array_p[j+6]
    array_soma[3] = array_p[0] + array_p[3] + array_p[6]
    array_soma[4] = array_p[1] + array_p[4] + array_p[7]
    array_soma[5] = array_p[2] + array_p[5] + array_p[8]
    array_soma[6] = array_p[0] + array_p[4] + array_p[8]
    array_soma[7] = array_p[2] + array_p[4] + array_p[6]
    if verificar_array_igual(array_soma): quadrados_magicos.append(array_p)

print('As combinações possíveis para os quadrados magicos 3x3 são: ')
for i in quadrados_magicos: print(i)
