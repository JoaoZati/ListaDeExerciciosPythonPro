#%% 04 - Quantas consoantes foram lidas

"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas 
consoantes foram lidas. Imprima as consoantes
"""

l_vogais = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P','Q',
            'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Z', 'Ç']
vetor = []
cont = 0
for _ in range(10):
    str_constante = input('Insira um caractere: ').upper()
    if str_constante in l_vogais:
        cont += 1
        vetor.append(str_constante)
        
print(f'As consoantes obtidas foram {vetor}')
