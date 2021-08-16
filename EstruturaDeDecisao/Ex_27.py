#%% 27 - tabela de preços frutaria

"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
    
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a 
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago
pelo cliente.
"""

peso_morango = float(input('Peso de Morangos: '))
peso_maça = float(input('Peso de Maças: '))

if peso_morango >= 5:
    preço_morango = peso_morango*2.2
else:
    preço_morango = peso_morango*2.5
    
if peso_maça >= 5:
    preço_maça = peso_maça*1.5
else:
    preço_maça = peso_maça*1.8
    
preço_final = preço_maça + preço_morango
peso_total = peso_maça + peso_morango

if preço_final >= 25 or peso_total >= 8:
    preço_final *= 0.9
    
print(f'Preço final a ser pago é de: R$ {preço_final}')
