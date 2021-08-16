#%% 12 - Alunos media de altura menor

"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que 
determine quantos alunos com mais de 13 anos possuem altura inferior à 
média de altura desses alunos.
"""

def input_numero_float_maior0(menssagem):
    while True:
        try:
            num = float(input(menssagem))
            if num <= 0: 
                print('Favor inseir um numero maior que zero')
                continue
            return num
        except ValueError:
            print('Favor inseir um numero')

def input_elementos_vetor(n, menssagem):
    vetor = []
    for i in range(n): 
        elemento = input_numero_float_maior0(f'Insira {n} {menssagem}, {menssagem} {i+1}: ')
        vetor.append(elemento)
    return vetor

elementos, vetores = 30, 2
dc_vetores = {}
dc_nomes = {0: 'Idades',
            1: 'Alturas'}       
for i in range(vetores): dc_vetores[i] = input_elementos_vetor(elementos, f'{dc_nomes[i]}')

media_altura = sum(dc_vetores[1]) / elementos
cont_alunos = 0
for i in range(elementos):
    if dc_vetores[0][i] > 13 and dc_vetores[1][i] < media_altura: cont_alunos += 1
