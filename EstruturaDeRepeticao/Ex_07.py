#%% 07 - Faça um programa que leia 5 números e informe o maior número

"""
Faça um programa que leia 5 números e informe o maior número
"""

lista_5 = []
numero = 0

while True:
    try:
        lista_5.append(float(input('Insira 5 numeros, numero {numero}: ')))
    except ValueError:
        print('Deve informar um numero real')
    else:
        numero += 1
        if numero >= 5:
            break
    
maior_5 = max(lista_5)
print(f'O maior numero é {maior_5}')
