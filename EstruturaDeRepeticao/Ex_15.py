#%% 15 - Fibonnaci até n

"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

while True:
    try:
        n = int(input('Insira um numero inteiro: '))
    except ValueError:
        print('Não foi fornecido um numero inteiro')
    else:
        break

a0 = 0
a1 = 0
fibo = 1

for i in range(1,n+1):
    if i != 1:
        fibo = a1 + a0
    print(f'{fibo}')
    a0 = a1
    a1 = fibo
