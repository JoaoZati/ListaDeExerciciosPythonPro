#%% 13 - Desenhar Moldura

"""
Desenha moldura. Construa uma função que desenhe um retângulo usando os 
caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, 
linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 
1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles 
devem ser modificados para valores dentro da faixa de forma elegante.
"""

def input_numero_inteiro_moldura():
    while True:
        try:
            num = int(input('Insira um numero inteiro, Entre 1 a 20: '))
            if 1 <= num <= 20: return num
            print('O numero tem que estar Entre 1 a 20')
        except ValueError:
            print('Favor inseir um numero inteiro')

linhas, colunas = input_numero_inteiro_moldura(), input_numero_inteiro_moldura()

for i in range(linhas):
    if i == 0 or i == linhas - 1: print(''.join(['−' for _ in range(colunas)]))
    else: print('|' + ''.join(['+' for _ in range(colunas - 2)]) + '|' )
    
