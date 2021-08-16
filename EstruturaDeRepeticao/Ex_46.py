#%% 46 - Competição de salto a distancia

"""
Em uma competição de salto em distância cada atleta tem direito a cinco 
saltos. No final da série de saltos de cada atleta, o melhor e o pior 
resultados são eliminados. O seu resultado fica sendo a média dos três 
valores restantes. Você deve fazer um programa que receba o nome e as 
cinco distâncias alcançadas pelo atleta em seus saltos e depois informe 
a média dos saltos conforme a descrição acima informada (retirar o 
 melhor e o pior salto e depois calcular a média). Faça uso de uma 
lista para armazenar os saltos. Os saltos são informados na ordem da 
execução, portanto não são ordenados. O programa deve ser encerrado 
quando não for informado o nome do atleta. A saída do programa deve ser 
conforme o exemplo abaixo:
    
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""


dc_salto = {'Primeiro Salto': 0,
'Segundo Salto': 0,
'Terceiro Salto': 0,
'Quarto Salto': 0,
'Quinto Salto': 0,}

l_salto = ['Primeiro Salto',
'Segundo Salto',
'Terceiro Salto',
'Quarto Salto',
'Quinto Salto']

def inserir_altura_salto(dc, l):
    i = 0
    while True:
        try:
            salto = float(input(f'{l[i]} (m): '))
            dc[l[i]] = salto
            i += 1
            if i >= len(l):
                break
        except ValueError:
            print('Deve ser informado um numero')
            

while True:
    nome = input('Atleta: ')
    if nome == '':
        break
    
    inserir_altura_salto(dc_salto, l_salto) 
    
    melhor_salto = max(dc_salto.values())
    pior_salto = min(dc_salto.values())
    
    soma_salto = 0
    for value in dc_salto.values():
        soma_salto += value
    soma_salto -= (melhor_salto + pior_salto) 
    media_salto = round(soma_salto / (len(l_salto) - 2) ,1)
    
    print(f'''
Melhor Salto: {melhor_salto} m
Pior salto: {pior_salto} m
Média dos demais saltos: {media_salto} m

Resultado final:
{nome}: {media_salto} m''')
