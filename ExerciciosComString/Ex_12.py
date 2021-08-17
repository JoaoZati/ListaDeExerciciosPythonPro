#%% 12 - Valide e Corrija o telefone

import sys

"""
Valida e corrige número de telefone. Faça um programa que leia um número 
de telefone, e corrija o número no caso deste conter somente 7 dígitos, 
acrescentando o '3' na frente. O usuário pode informar o número com ou 
sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""

telefone = input('Digite um telefone no formato XXXX-XXXX: ')

def validacao_telefone(telefone):
    telefone_lista = telefone.split('-')
    if len(telefone_lista[0]) not in [3,4]: return False, telefone_lista
    if len(telefone_lista[1]) != 4: return False, telefone_lista
    for num in telefone_lista:    
        try: num = int(num)
        except: return False, telefone_lista
    return True, telefone_lista

telefone_valido, telefone_lista = validacao_telefone(telefone)
novo_telefone = ''

if len(telefone_lista[0]) == 3 and telefone_valido: 
    novo_telefone = '3' + telefone_lista[0] + telefone_lista[1]

if novo_telefone:
    print(f'Telefone corrigido sem formatação: {novo_telefone}')
    print(f'Telefone corrigido com formatação: {novo_telefone[:4]}-{novo_telefone[4:]}')
    sys.exit()

if telefone_valido: print(f'Telefone válido {telefone}')
else: print('Telefone Inválido')
