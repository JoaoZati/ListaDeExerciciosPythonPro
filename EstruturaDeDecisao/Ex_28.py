#%% 28 - Hipermercado Tabajara descontos

"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:
    
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um
dos tipos de carne da promoção, porém não há limites para a quantidade 
de carne por cliente. Se compra for feita no cartão Tabajara o cliente 
receberá ainda um desconto de 5% sobre o total da compra. Escreva um 
programa que peça o tipo e a quantidade de carne comprada pelo usuário 
e gere um cupom fiscal, contendo as informações da compra: tipo e 
quantidade de carne, preço total, tipo de pagamento, valor do desconto 
e valor a pagar.
"""
import sys

peso_file = float(input("Inserir peso de File Duplo: "))
peso_alcatra = float(input("Inserir peso de Alcatra: "))
peso_picanha = float(input("Inserir peso de Picanha: "))

cartao_tabajara = input('Pagamento em catão tabajara? (digite "S" ou "N"): ').upper()

if cartao_tabajara == 'N':
    metodo_de_pagamento = 'Dinheio'
elif cartao_tabajara == 'S':
    metodo_de_pagamento = 'Cartão Tabajara'
else:
    print('Favor digitar "S" ou "N" na opção cartão tabajara')
    sys.exit()

preço_file_d = peso_file * 4.90
preço_file_sd = peso_file * 5.80

preço_alcatra_d = peso_alcatra * 5.90
preço_alcatra_sd = peso_alcatra * 6.80

preço_picanha_d = peso_picanha * 6.90
preço_picanha_sd = peso_picanha * 7.80

preço_disconto_file = preço_file_d + preço_alcatra_sd + preço_picanha_sd
preço_disconto_alcatra = preço_file_sd + preço_alcatra_d + preço_picanha_sd
preço_disconto_picanha = preço_file_sd + preço_alcatra_sd + preço_picanha_d

menor_preço_file_alcatra = min(preço_disconto_file,preço_disconto_alcatra)
menor_preço_file_picanha = min(preço_disconto_file,preço_disconto_picanha)
menor_preço_alcatra_picanha = min(preço_disconto_picanha,preço_disconto_alcatra)

preço_sem_disconto = preço_file_sd + preço_alcatra_sd + preço_picanha_sd
melhor_preço = min(preço_disconto_file,preço_disconto_alcatra,preço_disconto_picanha)

if peso_file >5 and peso_picanha > 5 and peso_alcatra > 5:
    preço_final = preço_sem_disconto
elif peso_alcatra <= 5 and peso_picanha <= 5:
    preço_final = menor_preço_alcatra_picanha
elif peso_alcatra <= 5 and peso_file <= 5:
    preço_final = menor_preço_file_alcatra
elif peso_file <= 5 and peso_picanha <= 5:
    preço_final = menor_preço_file_alcatra
else:
    preço_final = melhor_preço

if cartao_tabajara == "S":
    preço_final *= 0.95
    
desconto = preço_sem_disconto - preço_final

print(f"""
      Quantidade de carne comprada: 
      {peso_file} Kg de file, {peso_alcatra} Kg de Alcatra e {peso_picanha} Kg de Picanha 
      Metodo de Pagamento: {metodo_de_pagamento}
      Valor do desconto: R$ {desconto}
      Valor a pagar: R$ {preço_final}
      """)
