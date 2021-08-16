#%% 24 - Simulação Lancamento de dados

"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 
vezes e armazene os resultados em um vetor . Depois, mostre quantas 
vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) 
e uma função para gerar numeros aleatórios, simulando os lançamentos 
dos dados.
"""

from random import randint

lancamentos = 100
array_lancamentos = [randint(0, 5) for _ in range(lancamentos)]
soma_valores = [0]*6

for i in array_lancamentos:
    soma_valores[i] += 1   

print('')
for i in range(len(soma_valores)): print(f'Foi gerado {soma_valores[i]} lancamentos para o numero {i+1}')

