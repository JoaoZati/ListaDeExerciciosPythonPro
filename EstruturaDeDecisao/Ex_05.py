#%% 05 - Notas Parciais

"""
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
-A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
-A mensagem "Reprovado", se a média for menor do que sete;
-A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota_1 = float(input('Insira um Numero: '))
nota_2 = float(input('Insira outro número: '))

media = (nota_1 + nota_2)/2

if media <= 7.0:
    print('Reprovado')
elif media == 10.0:
    print('Aprovado com Excelência')
else:
    print('Aprovado')
