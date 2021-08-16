#%% 01 - Faça um Programa que peça dois números e imprima o maior deles.

numero_1 = float(input('Insira um Numero: '))
numero_2 = float(input('Insira outro número: '))

if numero_1 > numero_2:
    print(f'O maior numero é: {numero_1}')
elif numero_2 > numero_1:
    print(f'O maior numero é: {numero_2}')
else:
    print('Os numeros são iguais')
