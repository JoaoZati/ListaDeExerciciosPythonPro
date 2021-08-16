#%% 12 - Calculo Altura
"""
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: 
(72.7*altura) - 58
"""

altura = float(input('Digite a altura em metros: '))
peso_ideal = (72.7*altura) - 58

print(f'O peso ideial é de: {peso_ideal}')
