#%% 21 - Modelos de carros

"""
Faça um programa que carregue uma lista com os modelos de cinco carros 
(exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista 
com o consumo desses carros, isto é, quantos quilômetros cada um desses 
carros faz com um litro de combustível. Calcule e mostre:
    
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome 
para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma 
tela de exemplo. O disposição das informações deve ser o mais próxima 
possível ao exemplo. Os dados são fictícios e podem mudar a cada 
execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
"""

array_carros = ['fusca',
                'gol',
                'uno',
                'Vectra',
                'Peugeut']

array_consumos = [7,
                       10,
                       12.5,
                       9,
                       14.5]

custo_litro = 2.25
distancia = 1000
array_gastos = [round(distancia*custo_litro/consumo, 2) for consumo in array_consumos] 
array_distancia_per = [round(distancia/consumo, 1) for consumo in array_consumos]

print('')
print('Relatório Final')
for i in range(len(array_consumos)): 
    print(f'{i+1} - {array_carros[i]} - {array_consumos[i]} - {array_distancia_per[i]} litros - R$ {array_gastos[i]}')
    
menor_consumo = max(array_consumos)
array_maior_consumo = []
for i in range(len(array_carros)):
    if array_consumos[i] == menor_consumo: array_maior_consumo.append(array_carros[i])

print('O menor consumo é do ' + ', '.join([str(carro) for carro in array_maior_consumo]))    
