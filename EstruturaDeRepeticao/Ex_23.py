#%% 23 - Numeros primos entre 1 e N

"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um 
número inteiro fornecido pelo usuário. O programa deverá mostrar também 
o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes 
(divisões) executados.
"""

while True:
    try:
        num_p = int(input('Insira um numero inteiro N: '))
    except ValueError:
        print('Não foi fornecido um numero inteiro')
    else:
        if num_p < 0:
            print('numero precisa ser positivo')
        else:
            break

def VerificarSeEhPrimo(num):
    count = 0
    cont_div = 0
    for i in range(2, num):
        if num%i == 0:
            count += 1
        cont_div += 1
    
    if count == 0:
        return True, cont_div
    return False, cont_div
        
count_primo = 0
count_divisao = 0
list_primo = []

for i in range(2, num_p):
    bool_primo, divisoes = VerificarSeEhPrimo(i)
    if bool_primo:
        count_primo += 1
        list_primo.append(i)
    count_divisao += divisoes
        
if count_primo == 0:
    print(f'''
          Não Foram Encontrados Numeros primos entre 1 e {num_p}
          Total de divisões foi de {count_divisao}''')
elif count_primo == 1:
    print(f'''
          Foi Encontrado {count_primo} Numero primo entre 1 e {num_p}
          Total de divisões foi de {count_divisao}
          Os numeros encontrados são:''')
else:
    print(f'''
          Foram Encontrados {count_primo} Numeros primos entre 1 e {num_p}
          Total de divisões foi de {count_divisao}
          Os numeros encontrados são:''')
    for i in list_primo:
        print(i)
