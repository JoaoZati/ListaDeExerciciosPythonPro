#%% 16 - Vendedores x Comissões

"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga 
seus vendedores com base em comissões. O vendedor recebe $200 por semana 
mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um 
vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 
9 por cento de $3000, ou seja, um total de $470. Escreva um programa 
(usando um array de contadores) que determine quantos vendedores 
receberam salários nos seguintes intervalos de valores:
    
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie uma fórmula para chegar na posição da lista a partir do 
salário, sem fazer vários ifs aninhados.
"""

def input_salario_vendedor(menssagem):
    while True:
        try:
            num = float(input(menssagem))
            if num < 200: 
                print('Favor inseir um numero maior igual que 200')
                continue
            return num
        except ValueError:
            print('Favor inseir um numero')
            
def input_numero_vendedores():
    while True:
        try:
            num = int(input(f'Insira o numero de vendedores: '))
            if num <= 0: 
                print('Favor inseir um numero maior que zero')
                continue
            return num
        except ValueError:
            print('Favor inseir um numero inteiro')
            
lista_menores =    [200, 
    300 ,
    400 ,
    500 ,
    600 ,
    700 ,
    800 ,
    900 ,
    1000]

vendedores = input_numero_vendedores()
salarios = [] 
for i in range(vendedores): 
    salarios.append(input_salario_vendedor(f'Insira o salário do vendedor {i+1}: R$ '))

array_contador = [0 for _ in range(len(lista_menores))] 

for salario in salarios:
    for j in range(len(lista_menores)):
        if j == len(lista_menores) - 1:
            if salario >= lista_menores[j]: array_contador[j] += 1
        else:
            if salario >= lista_menores[j] and salario < lista_menores[j+1]: array_contador[j] += 1
        
print('')
for i in range(len(lista_menores)):
    if array_contador[i] == 0: continue
    if array_contador[i] == 1:
        if i == len(lista_menores) - 1: print(f'{array_contador[i]} vendedor ganha acima de {lista_menores[i]-1}')
        else: print(f'{array_contador[i]} vendedor ganha entre {lista_menores[i]} e {lista_menores[i+1]-1}')
        continue
    if i == len(lista_menores) - 1: print(f'{array_contador[i]} vendedores ganham acima de {lista_menores[i]-1}')
    else: print(f'{array_contador[i]} vendedores ganham entre {lista_menores[i]} e {lista_menores[i+1]-1}')
