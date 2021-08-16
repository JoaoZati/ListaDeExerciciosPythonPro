#%% 19 - dezenas, centenas e unidades

"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a 
quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre 
outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""          

numero_imp = int(input('Digite um numero entre 0 a 999: '))

def printunidadesnumero(num):
    if num < 0 or num > 999:
        print('O numero deve estar entre 0 e 999')
        return
    
    string_num = str(num)
    
    if num > 99:
        string = f'{string_num} = {string_num[0]} centenas, {string_num[1]} dezenas e {string_num[2]} unidades'
    elif num > 9:
            string = f'{string_num} = {string_num[0]} dezenas e {string_num[1]} unidades'
    else:
        string = f'{string_num} = {string_num[0]} unidades'
        
    print(string)
    
printunidadesnumero(numero_imp)
