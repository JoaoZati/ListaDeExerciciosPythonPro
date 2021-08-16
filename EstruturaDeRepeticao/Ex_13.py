#%% 13 - Primeiro elevado ao segundo sem expoente

"""
Faça um programa que peça dois números, base e expoente, calcule e 
mostre o primeiro número elevado ao segundo número. Não utilize a 
função de potência da linguagem.
"""

num_1 = 2
num_2 = 5

while True:
    try:
        num_1 = float(input('Insira um numero: '))
        num_2 = float(input('Insira a exponencial: '))
    except ValueError:
        print('Valor inserido não é um numero')
    else:
        break

incremento = 1
num_1_elev = num_1
while incremento < num_2:
    num_1_elev *= num_1
    incremento += 1
    
print(f'{num_1_elev}')
