#%% 22 - Se nao é primo quem divide

"""
Altere o programa de cálculo dos números primos, informando, caso o 
número não seja primo, por quais número ele é divisível.
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
list_div = []
for i in range(1, num_p + 1):
    if num_p%i == 0:
        count += 1
        if i != 1 and i != num_p:
            list_div.append(i)

if count == 2:
    print(f'{num_p} é um Numero é primo')
else:
    print(f'{num_p} não é um numero primo e pode ser dividido por:')
    for i in list_div:
        print(f'{i}')
