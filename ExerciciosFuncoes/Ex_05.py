#%% 05 - somaImposto

"""
Faça um programa com uma função chamada somaImposto. A função possui 
dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre 
vendas expressa em porcentagem e custo, que é o custo de um item antes 
do imposto. A função “altera” o valor de custo para incluir o imposto 
sobre vendas.
"""

def inserir_numero_sistema(menssagem):
    while True:
        try:
            numero = float(input(menssagem))
            return numero
        except ValueError:
            print('Informe um numero inteiro')
            
taxa = inserir_numero_sistema('Inserir Taxa de Imposto (%): ')
custo = inserir_numero_sistema('Inserir custo (R$): ')
            
def somaImposto(taxaImposto, custo):
    taxaImposto /= 100
    return custo *(1 + taxaImposto)

print(somaImposto(taxa, custo))
