#%% 48 - Inverter Numero

"""
Faça um programa que peça um numero inteiro positivo e em seguida 
mostre este numero invertido.

Exemplo:
  12376489
  => 98467321
"""

def input_numero_inteiro():
    while True:
        try:
            num = int(input('Insira um numero inteiro, positivo: '))
            if num <= 0:
                print('O numeo tem que ser positivo')
                continue
            num = str(num)
            return num
        except ValueError:
            print('Favor inseir um numero inteiro')

string = '12345'
        
def inverter_string(string):
    invertido = ''
    while True:
        invertido += string[-1]
        string = string[:-1]
        if string == '':
            return invertido
        
str_num = input_numero_inteiro()
str_inv = inverter_string(str_num)
print(str_inv)
