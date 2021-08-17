#%% 09 - Reverso do número. (inverso)

""" 
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
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
