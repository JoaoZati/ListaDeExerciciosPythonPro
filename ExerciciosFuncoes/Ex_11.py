#%% 11 - Data do mês por extenso

"""
Data com mês por extenso. Construa uma função que receba uma data no 
formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso 
de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja 
inválida.
"""

mes_extenso = ['janeiro',
             'fevereiro'
             'março',
             'abril',
             'maio',
             'junho',
             'julho',
             'agosto',
             'setembro',
             'outubro',
             'novembro',
             'dezembro']

def verificar_se_bixesto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def verificar_data_valida(ano, mes, dia):
    if (not -9999 <= ano <= 9999) or (not 0 < mes <= 12) or (not 0 < dia <= 31): return False
    
    fim_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
    if verificar_se_bixesto(ano): fim_mes[1] = 29
    
    return (dia <= fim_mes[mes - 1])

bool_data = verificar_data_valida(2001, 2, 29)

while True:
    try:
        dia, mes, ano = input('Digite uma data no formato DD/MM/AAAA: ').split('/')
        dia, mes, ano = int(dia), int(mes), int(ano)
        break
    except ValueError:
        print('Favor informar no formato DD/MM/AAAA e usar "/" como separação')
        
if verificar_data_valida(ano, mes, dia): print(f'{dia} de {mes_extenso[mes -1]} de {ano}')
else: print('Data Inválida')
