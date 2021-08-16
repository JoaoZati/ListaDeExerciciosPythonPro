#%% 47 - Ginastica votação

"""
Em uma competição de ginástica, cada atleta recebe votos de sete 
jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a 
média dos votos restantes. Você deve fazer um programa que receba o 
nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em 
sua apresentação e depois informe a sua média, conforme a descrição 
acima informada (retirar o melhor e o pior salto e depois calcular a 
média com as notas restantes). As notas não são informados ordenadas. 
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
    
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""
import numpy as np
 
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

def inserir_nota_media():
    i = 0
    array_notas = np.array(range(7), dtype = 'float') 
    while True:
        try:
            nota = float(input('Nota: '))
            array_notas[i] = nota
            i += 1
            if i >= 7:
                break
        except ValueError:
            print('Deve ser informado um numero')
    
    return array_notas
            
while True:
    nome = input('Atleta: ')
    if nome == '':
        break
    
    array_notas = inserir_nota_media()
    melhor_nota = max(array_notas)
    pior_nota = min(array_notas)
    media_nota = (array_notas.sum() - (melhor_nota + pior_nota))/(len(array_notas)-2)
    
    print(f'''
Resultado final:
Atleta: {nome}
Melhor Nota: {melhor_nota} 
Pior Nota: {pior_nota} 
Média dos demais Notas: {media_nota} m''')  
