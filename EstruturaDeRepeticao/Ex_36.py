#%% 36 - Tabuada com imput

"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro 
que será digitado pelo usuário, mas a tabuada não deve necessariamente 
iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
informados também pelo usuário, conforme exemplo abaixo:
    
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
"""

while True:
    try:
        tabuada = int(input('Montar a tabuada de: '))
        if not 0 < tabuada <= 10:
            print('digite um valor de 1 a 10')
            continue
        comeco = int(input('Começar por: '))
        if not 0 < comeco <= 10:
            print('digite um valor de 1 a 10')
            continue
        fim = int(input('Terminar em: '))
        if not 0 < fim <= 10:
            print('digite um valor de 1 a 10')
            continue
        break
    except ValueError:
        print('Não foi fornecido um numero inteiro')
        
print(f'Vou montar a tabuada de {tabuada} começando em {comeco} e terminando em {fim}: ')        
for i in range(comeco, fim + 1):
    resultado = tabuada * i
    print(f'{tabuada} X {i} = {resultado}')
