#%% 12- Desenvolvedor de Tabuada

"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer 
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele 
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

while True:
    try:
        numero_tabuada = int(input('Insira um numero entre 1 a 10: '))
    except ValueError:
        print('Valor inserido não é um numero inteiro')
    else:
        if 1 <= numero_tabuada <= 10:
            break
        print('Numero não está entre 1 a 10')

for i in range(1,11):
    mult = numero_tabuada*i
    print(f'{numero_tabuada} X {i} = {mult}')
