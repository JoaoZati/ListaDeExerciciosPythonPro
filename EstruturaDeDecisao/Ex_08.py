#%% 08 - Menor Preço

"""
Faça um programa que pergunte o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais
 barato.
"""

numero_1 = float(input('Insira o preço do primeiro produto: '))
numero_2 = float(input('Insira o preço do segundo produto: '))
numero_3 = float(input('Insira o preço do terceiro produto: '))

minimo = min(numero_1, numero_2, numero_3)

string = ''
lista_num = [numero_1, numero_2, numero_3]
lista_ordem = ['primeiro', 'segundo', 'terceiro']
for i in list(range(len(lista_num))):
    if minimo == lista_num[i]:
        string = string + f', {lista_ordem[i]} produto'

print(f'O produto mais barato é para compra é o{string}')
