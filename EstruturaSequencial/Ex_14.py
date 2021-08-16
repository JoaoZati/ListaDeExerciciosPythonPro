#%% 14 - João e os peixes

"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um 
peso de peixes maior que o estabelecido pelo regulamento de pesca do 
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por 
quilo excedente. João precisa que você faça um programa que leia a 
variável peso (peso de peixes) e calcule o excesso. Gravar na variável 
excesso a quantidade de quilos além do limite e na variável multa o 
valor da multa que João deverá pagar. Imprima os dados do programa com 
as mensagens adequadas.
"""

peso_peixes = float(input('Insira o peso total da pescaria: '))

def calculoexcessodepeso(peso_p):
    excesso_peso = peso_p - 50
    
    if excesso_peso <= 0:
        print('Não ouve excesso de peso')
        return 
    
    excesso_multa = excesso_peso*4
    
    print(f'O excesso de peso foi de: {excesso_peso} Kg')
    print(f'A multa a ser paga é de: R$ {excesso_multa}')
    
calculoexcessodepeso(peso_peixes)
