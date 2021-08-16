#%% 06 - media maior ou igual a 7

"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e 
armazene num vetor a média de cada aluno, imprima o número de alunos 
com média maior ou igual a 7.0.
"""
import numpy as np

def input_numero_float(menssagem):
    while True:
        try:
            num = float(input(menssagem))
            if num < 0 or num > 10: 
                print('Inserir nota entre 0 e 10') 
                continue
            return num
        except ValueError:
            print('Favor inseir um numero')

def input_vetor_floats(tamanho, menssagem):
    vetor = []
    for i in range(tamanho):
        numero = input_numero_float(menssagem + f'{i+1}: ')
        vetor.append(numero)
    return vetor

medias = []
medias_maior_7 = []
for i in range(10):
    vetor = input_vetor_floats(4, f'Inserir as 4 notas do aluno {i+1}, nota ')
    media = np.array(vetor).mean()
    if media >= 7: medias_maior_7.append(media)
    medias.append(media)
    
print(f'Os alunos com nota maior igual a 7 é {len(medias_maior_7)}')
