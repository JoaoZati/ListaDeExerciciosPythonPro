#%% 49 - N termos

"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
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
m = 0
S = 0
for n in range(n):
    n += 1
    m += n
    print(f'{S} += {n}/{m}')
    S += n / m
    
print(S)
