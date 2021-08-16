#%% 04 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

soma = 0
for i in list(range(1,5)):
    nota = float(input(f'Digite a nota {i}: '))
    soma += nota
    
media = soma/4
    
print(f'A media das notas é igual a: {media}')
