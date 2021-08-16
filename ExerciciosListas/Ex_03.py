#%% 03 - Mostrar notas e medias
import numpy as np

def input_numero_float(menssagem):
    while True:
        try:
            num = float(input(menssagem))
            return num
        except ValueError:
            print('Favor inseir um numero')

def input_vetor_floats(tamanho, menssagem):
    vetor = []
    for _ in range(tamanho):
        numero = input_numero_float(menssagem)
        vetor.append(numero)
    return vetor

media_notas = input_vetor_floats(4, 'Insira 4 notas: ') 
array_medias = np.array(media_notas).mean()
print(f'{array_medias}')
