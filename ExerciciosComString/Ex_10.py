#%% 10 - Numero por Extenso

import sys

def input_numero_inteiro_extenso():
    while True:
        try:
            num = int(input('Insira um numero inteiro, Entre 0 a 99: '))
            if 0 <= num <= 99: return num
            print('O numero tem que estar Entre 0 a 99')
        except ValueError:
            print('Favor inseir um numero inteiro')

numero = input_numero_inteiro_extenso()

array_decimal = ['',
                 'Dez',
                 'Vinte',
                 'Trinta',
                 'Quarenta',
                 'Cinquenta',
                 'Sessenta',
                 'Setenta',
                 'Oitenta',
                 'Noventa']

array_unidade = ['',
                 'Um',
                 'Dois',
                 'Três',
                 'Quatro',
                 'Cinco',
                 'Seis',
                 'Sete',
                 'Oito',
                 'Nove']

array_dez = ['Onze',
             'Doze',
             'Treze',
             'Quatorse',
             'Quinze',
             'Dezesseis',
             'Dezessete',
             'Dezoito',
             'Dezenove',
             ]

decimais, unidades = divmod(numero, 10)

string_dez = ''
for i in range(len(array_decimal)):
    if decimais == 1 and unidades != 0: string_dez = array_dez[unidades-1]     
    if i == decimais: decimal = i
    if i == unidades: unidade = i
    
if unidade == 0 and decimal == 0:
    print('Zero')
    sys.exit()
    
if string_dez: print(f'{string_dez}')
else: 
    if unidades == 0 or decimal == 0: print(f'{array_decimal[decimal]}{array_unidade[unidade]}')
    else: print(f'{array_decimal[decimal]} e {array_unidade[unidade]}')
