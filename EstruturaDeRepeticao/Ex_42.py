#%% 42 - Quantidade positivos
    
"""
Faça um programa que leia uma quantidade indeterminada de números 
positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá 
terminar quando for lido um número negativo.
"""

def imputfloat(mensagem):
    while True:
        try:
            inp = float(input(mensagem))
            return inp
        except ValueError:
            print('Insira um numero')
            
soma_0_25 = soma_26_50 = soma_51_75 = soma_76_100 = 0   
 
dic_result = {'0_25': 0,
              '26_50': 0,
              '51_75': 0,
              '76_100': 0}

dic_somas = {'0_25': [0,25],
             '26_50': [25,50],
             '51_75': [51,75],
             '76_100': [76,100],}   
while True:
    try:
        num = imputfloat('Digite um numero "para sair digite um numero negativo": ')
        if num < 0:
            break
        for key,value in dic_somas.items():
            if value[0] <= num <= value[1]:
                dic_result[key] += 1
    except Exception as e: print(e)
    
for key, value in dic_result.items():
    print(f'existem {value} numeros no intervalo de: {key}')
