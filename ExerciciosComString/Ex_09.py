#%% 09 - Validação de CPF

"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de 
um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número 
válido ou inválido através da validação dos dígitos verificadores edos 
caracteres de formatação.
"""

cpf = input('Digite o CPF no modelo xxx.xxx.xxx-xx: ')

array_cpf = cpf.split('.')
array_digito = array_cpf[-1].split('-')
array_cpf_final = array_cpf[:-1] + array_digito

def verificacao_cpf(array):
    for i in range(len(array)):
        if i == len(array) - 1:
            if len(array[i]) != 2: return False
            continue
        if len(array[i]) != 3: return False          
    for num in array:
        try: num = int(num)
        except: return False
    return True

if verificacao_cpf(array_cpf_final): print('CPF Válido')
else: print('CPF Invalido')

len(array_cpf_final[2])
