#%% 21 - Calculo numero primo

"""
Faça um programa que peça um número inteiro e determine se ele é ou não 
um número primo. Um número primo é aquele que é divisível somente por 
ele mesmo e por 1.
"""

while True:
    try:
        num_p = int(input('Insira um numero inteiro N: '))
    except ValueError:
        print('Não foi fornecido um numero inteiro')
    else:
        if num_p < 0:
            print('numero precisa ser positivo')
        else:
            break

count = 0
for i in range(1, num_p + 1):
    if num_p%i == 0:
        count += 1

if count == 2:
    print(f'{num_p} é um Numero é primo')
else:
    print(f'{num_p} não é um numero primo')
