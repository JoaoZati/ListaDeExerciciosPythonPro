#%% 34 - Primo Verificacao

"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver 
um programa que leia as um conjunto indeterminado de temperaturas, e 
informe ao final a menor e a maior temperaturas informadas, bem como a 
média das temperaturas.
"""

while True:
    try:
        num_p = int(input('Insira um numero inteiro N: '))
    except ValueError:
        print('Não foi fornecido um numero inteiro')
    else:
        if num_p <= 0:
            print('numero precisa ser positivo e maior que zero')
        else:
            break

count = 0
for i in range(2, num_p):
    if num_p%i == 0:
        count += 1

if count == 0:
    print(f'{num_p} é um Numero é primo')
else:
    print(f'{num_p} não é um numero primo')
