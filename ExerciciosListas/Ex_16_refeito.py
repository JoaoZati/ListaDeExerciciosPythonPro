#%% 16 - (Refeito)

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
            
vendedores = input_numero_vendedores()
salarios = [] 
for i in range(vendedores): 
    salarios.append(input_salario_vendedor(f'Insira o salário do vendedor {i+1}: R$ '))

contagem_da_faixa_salarial = [0]*9 #concatenando todos os elementos

for salario in salarios:
    indice = salario // 100 - 2
    indice_maximo = len(contagem_da_faixa_salarial) -1
    indice = int(min(indice, indice_maximo))
    contagem_da_faixa_salarial[indice] += 1

constante = 200    
for i in range(len(contagem_da_faixa_salarial)):
    if contagem_da_faixa_salarial[i] != 0:
        if contagem_da_faixa_salarial[i] == 1: 
            if contagem_da_faixa_salarial[i] >= 1000: print(f'Acima de R$ {constante+(i*100)} existe {contagem_da_faixa_salarial[i]} salario')
            print(f'Entre R$ {constante+(i*100)} e R$ {constante + (i+1)*100 - 1} existe {contagem_da_faixa_salarial[i]} salario')
        else:
            if contagem_da_faixa_salarial[i] >= 1000: print(f'Acima de R$ {constante+(i*100)} existem {contagem_da_faixa_salarial[i]} salarios')
            print(f'Entre R$ {constante + (i*100)} e R$ {constante + (i+1)*100 - 1} existem {contagem_da_faixa_salarial[i]} salarios')
