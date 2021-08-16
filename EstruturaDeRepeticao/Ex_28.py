#%% 28 - Coleção de CD

"""
Faça um programa que calcule o valor total investido por um colecionador 
em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário 
deverá informar a quantidade de CDs e o valor para em cada um.
"""

while True:
    try:
        n = int(input('Insira o numero da sua coleção de cds: '))
        if n <= 0:
            print('Numero precisa ser maior que 0')
            continue
        break
    except ValueError:
        print('Não foi fornecido um numero inteiro')

soma = 0
cont = 1
while True:
    try:
        preco = float(input(f'Insira o preço do CD {cont}: '))
        if preco < 0:
            print('Insira um valor positivo')
            continue
        
        soma += preco
        media = soma/cont
        print(f'A media da sua coleção de CDS é: {media}')
        
        cont += 1
        if cont > n: 
            break
    except ValueError:
        print('Favor insira um numero')
