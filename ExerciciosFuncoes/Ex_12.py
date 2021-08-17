#%% 12 - Embaralha palavra

"""
Embaralha palavra. Construa uma função que receba uma string como 
parâmetro e devolva outra string com os carateres embaralhados. Por 
exemplo: se função receber a palavra python, pode retornar npthyo, 
ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos os caracteres serão devolvidos em 
caixa alta ou caixa baixa, independentemente de como foram digitados.
"""
from random import randint

palavra_entrada = input('Digite uma palavra: ')

def embaralhar_palavra(palavra_entrada):
    palavra_aleatoria = ''
    while True:
        if palavra_entrada == '': return palavra_aleatoria
        i = randint(0, len(palavra_entrada) - 1)
        palavra_aleatoria += palavra_entrada[i]
        palavra_entrada = palavra_entrada[:i] + palavra_entrada[(i + 1):]
        

palavra_embaralhada = embaralhar_palavra(palavra_entrada)
print(f'A palavra embaralhada é {palavra_embaralhada}')
