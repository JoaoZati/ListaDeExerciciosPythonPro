#%% 17 - Fatorial

"""
Faça um programa que calcule o fatorial de um número inteiro fornecido 
pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""    

while True:
    try:
        num_f = int(input('Insira um numero inteiro: '))
    except ValueError:
        print('Não foi fornecido um numero inteiro')
    else:
        break

string = f'{num_f}!='
fatorial = 1

for i in range(num_f, 0, -1):
    string += f'{i}'
    fatorial *= i
    if i == 1:
        string += '='
    else:
        string += '.'
        

string += f'{fatorial}'
print(f'{string}') 
