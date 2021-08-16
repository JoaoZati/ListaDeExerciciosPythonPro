#%% 07 - Faça um Programa que leia três números e mostre o maior e o menor deles.

numero_1 = float(input('Insira um Numero: '))
numero_2 = float(input('Insira outro número: '))
numero_3 = float(input('Insira outro número: '))

maximo = max(numero_1, numero_2, numero_3)
minimo = min(numero_1, numero_2, numero_3)

print(f'O maior numero é {maximo}, e o menor é {minimo}')
