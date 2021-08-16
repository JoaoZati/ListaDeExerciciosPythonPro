#%% 20 - Calculo Fatorial varias vezes

"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
o fatorial várias vezes e limitando o fatorial a números inteiros 
positivos e menores que 16.
"""
import sys

while True:
    while True:
        try:
            num_f = int(input('Insira um numero inteiro entre 1 e 16: '))
        except ValueError:
            print('Não foi fornecido um numero inteiro')
        else:
            if num_f < 1 or num_f > 16:
                print('Favor digite um numero entre 1 e 16')
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
    
    continuar = input("Deseja continuar a calcular fatorial? (Se sim digite 'S'): ").upper()
    if continuar != 'S':
        sys.exit()
