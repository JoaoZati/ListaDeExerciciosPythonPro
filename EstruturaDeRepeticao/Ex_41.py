#%% 41 - Juros parcelado

"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela 
com os seguintes dados: valor da dívida, valor dos juros, quantidade de 
parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67

"""

def imputfloat_maior0(mensagem):
    while True:
        try:
            inp = float(input(mensagem))
            if inp <= 0:
                print('O valor tem que ser maior que zero')
                continue
            return inp
        except ValueError:
            print('Insira um numero')
            
divida = imputfloat_maior0('Digite o valor da divida: ')

dic_tabela = {1: 0,
              3: 10,
              6: 15,
              9: 20,
              12: 25,
              }

print('Valor da Divida - Valor do Juros - Quantidade de Parcelas - Valor da Parcela')
for key,value in dic_tabela.items():
    valor_juros = (value/100) * divida
    final_juros = round(divida + valor_juros)
    parcela = round(final_juros / key, 2)
    
    print(f'{final_juros}  -  {valor_juros}  -  {key}  -  {parcela}')
    
