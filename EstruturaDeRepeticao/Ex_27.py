#%% 27 - Media Turmas e Quantidades Alunos

"""
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para 
cada turma. As turmas não podem ter mais de 40 alunos.
"""
import numpy as np

def VerificaSeLimitesAlunos(alunos):
    if not 1 <= alunos <= 40:
        print('Alunos deves estar entre 1 e 40')
        return True

def VerificaSeLimitesDeNotas(notas):
    if not 1 <= notas <= 40:
        print('Notas devem estar entre 0 e 10')
        return True
    
def InserirNotasDosAlunosNoDicionario(num, dicionario, turma):
    dicionario[turma] = []
    cont = 1
    while True:
        try: 
            nota = float(input(f'Insira o valor da nota de 0 a 10 do aluno {cont} da truma {turma}: '))
            if VerificaSeLimitesDeNotas(nota):
                continue
            dicionario[turma].append(nota)
            cont += 1
            if cont > num:
                break
        except ValueError:
            print('A nota deve ser um numero')
            
while True:
    try:
        n = int(input('Insira o numero de turmas: '))
        if n <= 0:
            print('Numero precisa ser maior que 0')
            continue
        break
    except ValueError:
        print('Não foi fornecido um numero inteiro')

dic_turma = {}    
turma = 1
while True:
    try:
        num = int(input(f'Insira o numero de alunos na turma {turma}: '))
        if VerificaSeLimitesAlunos(num):
            continue
        InserirNotasDosAlunosNoDicionario(num, dic_turma, turma)
        turma += 1
        if turma > n:    
            break
    except ValueError:
        print('Não foi fornecido um numero inteiro para numero de alunos e real para as notas')

for key, value in dic_turma.items():
    media = np.array(value).mean()
    print(f'A media da Turma {key} foi de: {media}')
