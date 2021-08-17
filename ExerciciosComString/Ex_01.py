#%% 01 - Tamanho String

"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o 
conteúdo delas seguido do seu comprimento. Informe também se as duas 
strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

print('Compara duas strings')

s1 = input('String 1: ')
s2 = input('String 2: ')

tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'Taamanho de {s1}: {tamanho1}')
print(f'Taamanho de {s2}: {tamanho2}')

comparacao_tamanhos = 'diferentes'
comparacao_conteudo = 'diferentes'

if s1 == s2:  comparacao_tamanhos = comparacao_conteudo = 'iguais'
elif tamanho1 == tamanho2: comparacao_tamanhos = 'iguais'

print(f'As duas strings são de tamanhos {comparacao_tamanhos}.')
print(f'As duas strings possuem conteúdo {comparacao_conteudo}.')
