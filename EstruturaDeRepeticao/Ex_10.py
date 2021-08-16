#%% 10 - Numero entre inteiros

"""
Faça um programa que receba dois números inteiros e gere os números 
inteiros que estão no intervalo compreendido por eles.
"""

while True:
    try:
        num_1 = int(input('Digite um numero inteiro: '))
        num_2 = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('Os Numeros tem que ser inteiros')
    else:
        break

minimo = min(num_1, num_2)
maximo = max(num_1, num_2)

print(f'Os numeros entre {num_1} e {num_2} é: ')
for i in range(minimo + 1, maximo):
    print(i)
