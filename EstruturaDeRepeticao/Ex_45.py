#%% 45 - Gabarito prova alunos Simples

"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 
10 questões, o programa deve perguntar ao aluno a resposta de cada 
questão e ao final comparar com o gabarito da prova e assim calcular o 
total de acertos e a nota (atribuir 1 ponto por resposta certa). Após 
cada aluno utilizar o sistema deve ser feita uma pergunta se outro 
aluno vai utilizar o sistema. Após todos os alunos terem respondido 
informar:
    
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.

Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
"""

""" 
#teste gabarito
dic_gabarito = {
1: 'A',
2: 'B',
3: 'C',
4: 'D',
5: 'E',
6: 'E',
7: 'D',
8: 'C',
9: 'B',
10: 'A'}
"""
    
l_questoes = ['A','B','C','D','E']

def imput_questao(menssagem, l):
    while True:
        inp = input(menssagem).upper()
        if inp not in l:
            print('Favor Digite "A", "B", "C", "D" ou "E"')
            continue
        return inp
    
def inserir_o_gabarito():
    print('Inserir o gabarito')
    dc = {}
    for i in range(1,11):
        questao = imput_questao(f'Insira o gabarito para a questão {i}: ', l_questoes)
        dc[i] = questao
    return dc

dic_gabarito = inserir_o_gabarito()

def nota_do_aluno():
    soma_nota = 0
    for key, value in dic_gabarito.items():
        resp = imput_questao(f'Insira a Resposta para a questão {key}: ', l_questoes)
        if resp == value:
            soma_nota += 1
    return soma_nota

maior_acerto = contagem = soma_turma = 0
menor_acerto = 10
while True:
    continuar = input('Digite "E" para encerrar, para continuar digite qualquer tecla: ').upper()
    if continuar == 'E':
        break
    
    contagem += 1
    print(f'Insira as Respostas do aluno {contagem}: ')
    nota_aluno = nota_do_aluno()
    soma_turma += nota_aluno
    media_turma = round(soma_turma / contagem, 2)
    maior_acerto = max(maior_acerto, nota_aluno)
    menor_acerto = min(menor_acerto, nota_aluno) 
    
    print('')
    print(f'O maior acerto é de {maior_acerto} e o menor acerto é de {menor_acerto}')
    print(f'O total de alunos que utilizaram o sistema é de {contagem}')
    print(f'A média da turma é de {media_turma}')
    
