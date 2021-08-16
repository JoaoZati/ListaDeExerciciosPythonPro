#%% 21 - programa para saque no banco

"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar 
ao usuário a valor do saque e depois informar quantas notas de cada 
valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 
100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O 
programa não deve se preocupar com a quantidade de notas existentes na 
máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas 
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três 
notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
import math

saque_imp = int(input('Digite um valor para saque de R$ 10,00 a R$ 600,00: '))

def FuncaoDicionarioNotas(quantidade, nota, dicionario):
    if quantidade == 1:
        unidade = f'nota de R$ {nota}'
        dicionario[unidade] = quantidade
    elif quantidade > 1:
        unidade = f'notas de R$ {nota}'
        dicionario[unidade] = quantidade

def valorparasaque(saque):
    if saque < 10 or saque > 600:
        print('Limites minimo de R$ 10 e máximo de R$ 600')
    
    p_saque = saque
        
    quantidade_100 = math.floor(p_saque/100)
    p_saque -= quantidade_100*100
    
    quantidade_50 = math.floor(p_saque/50)
    p_saque -= quantidade_50*50
    
    quantidade_10 = math.floor(p_saque/10)
    p_saque -= quantidade_10*10
    
    quantidade_5 = math.floor(p_saque/5)
    p_saque -= quantidade_5*5
    
    dict_notas = {}
    FuncaoDicionarioNotas(quantidade_100, 100, dict_notas)
    FuncaoDicionarioNotas(quantidade_50, 50, dict_notas)
    FuncaoDicionarioNotas(quantidade_10, 10, dict_notas)
    FuncaoDicionarioNotas(quantidade_5, 5, dict_notas)
    FuncaoDicionarioNotas(p_saque, 1, dict_notas)
    
    return dict_notas

def printdicionario(dicionario):
    lista_keys = []
    for key in dicionario.keys():
        lista_keys.append(f'{dicionario[key]} {key}, ')
        
    lista_keys[-1] = lista_keys[-1][:-2] + '.'
    lista_keys[-2] = lista_keys[-2][:-2] + ' e '
    
    string_final = ''
    for key in lista_keys:
        string_final += key
    
    print(f'{string_final}')

def printdicionario_simples(dicionario):
    for key in dicionario.keys():
        print(f'{dicionario[key]} {key}')

dicionario_notas = valorparasaque(saque_imp)
#printdicionario_simples(dicionario_notas)
printdicionario(dicionario_notas)

#sorted([1,2,5,8,96,1,5], key = int, reverse=True) #(usar para inverter, acabei n usando)
