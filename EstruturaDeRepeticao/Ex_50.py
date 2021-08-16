#%% 50 - H com N termos

"""
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule 
o valor de H com N termos.

"""

def input_numero_inteiro():
    while True:
        try:
            num = int(input('Insira um numero inteiro, positivo: '))
            if num <= 0:
                print('O numeo tem que ser positivo')
                continue
            return num
        except ValueError:
            print('Favor inseir um numero inteiro')

n = input_numero_inteiro()
H = 0
for n in range(n):
    n += 1
    print(f'{H} += 1 / {n}')
    H += 1 / n
    
print(H)
