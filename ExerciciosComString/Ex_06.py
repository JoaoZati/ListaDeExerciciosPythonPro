#%% 06 - Data por Extenso

"""
Data por extenso. Faça um programa que solicite a data de nascimento 
(dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""

mes_extenso = ['Janeiro',
             'Fevereiro'
             'Março',
             'Abril',
             'Maio',
             'Junho',
             'Julho',
             'Agosto',
             'Setembro',
             'Outubro',
             'Novembro',
             'Dezembro']

while True:
    try:
        dia, mes, ano = input('Digite uma data no formato DD/MM/AAAA: ').split('/')
        dia, mes, ano = int(dia), int(mes), int(ano)
        break
    except ValueError:
        print('Favor informar no formato DD/MM/AAAA e usar "/" como separação')
        
print(f'Você nasceu em {dia} de {mes_extenso[mes -1]} de {ano}')
