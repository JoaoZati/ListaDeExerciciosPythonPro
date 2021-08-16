#%% 25 - Media de idades
"""
Faça um programa que peça para n pessoas a sua idade, ao final o 
programa devera verificar se a média de idade da turma varia entre 
0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, 
adulta ou idosa, conforme a média calculada.
"""
import sys
import numpy as np

while True:
    try:
        n = int(input('Insira o numero de idades calcular a média: '))
        if n <= 0:
            print('Numero precisa ser maior que 0')
            continue
        break
    except ValueError:
        print('Não foi fornecido um numero inteiro')

lista_n = []
numero = 0
while True:
    try:
        num = int(input(f'Insira {n} idades maior que 0, idade numero {numero + 1}: '))
        if num <= 0:
            print('O valor da idade tem que ser maior que zero')
            continue
        lista_n.append(num)
        numero += 1
        if numero >= n:
            break
    except ValueError:
        print('Deve informar um numero inteiro')
        
numpy_lista = np.array(lista_n)
num_media = numpy_lista.mean()

if num_media <= 25:
    print(f'Media de idade menor que 25 anos, media: {num_media}')
    sys.exit()
elif 25 < num_media <= 60:
    print(f'Media de idade esta entre 26 a 60 anos, media: {num_media}')
    sys.exit()
    
print(f'Media de idade tem mais que 60 anos, media: {num_media}')
