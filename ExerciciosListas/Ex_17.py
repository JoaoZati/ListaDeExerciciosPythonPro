#%% 17 - Salto a Distancia

"""
Em uma competição de salto em distância cada atleta tem direito a cinco 
saltos. O resultado do atleta será determinado pela média dos cinco 
valores restantes. Você deve fazer um programa que receba o nome e as 
cinco distâncias alcançadas pelo atleta em seus saltos e depois informe 
o nome, os saltos e a média dos saltos. O programa deve ser encerrado 
quando não for informado o nome do atleta. A saída do programa deve ser 
conforme o exemplo abaixo:
    
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
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
    
    media_salto = sum(dc_salto.values()) / len(dc_salto)
    melhor_salto = max(dc_salto.values())
    pior_salto = min(dc_salto.values())

    print(f'''
Resultado final:
Atleta: {nome}

Melhor Salto: {melhor_salto} m
Pior salto: {pior_salto} m
Saltos: {' - '.join(str(value) for value in dc_salto.values())}
Média dos Saltos: {media_salto} m
''')
