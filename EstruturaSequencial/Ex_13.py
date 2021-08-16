#%% 13 - Peso Ideial Homem x Mulher

"""
Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
    
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

"""

altura = float(input('Digite a altura em metros: '))
genero = input('Insira o genero. Digite H para homem ou M para Mulher: ')

if genero != 'H' and genero != 'M':
    print('''
          Input Errado use H para Homem e M para Mulher: 
          verefique o uso de capslock ''')
        
peso_ideal_H = (72.7*altura) - 58
peso_ideal_M = (62.1*altura) - 44.7

if genero == 'H':    
    print(f'O peso ideial é de: {peso_ideal_H}')
elif genero == 'M':
    print(f'O peso ideial é de: {peso_ideal_M}')
