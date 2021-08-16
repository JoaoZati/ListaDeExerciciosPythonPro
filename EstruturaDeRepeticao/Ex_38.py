#%% 38 - Salario e seu aumento

"""
Um funcionário de uma empresa recebe aumento salarial anualmente: 
Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de 
R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem 
ao dobro do percentual do ano anterior. Faça um programa que determine 
o salário atual desse funcionário. Após concluir isto, altere o 
programa permitindo que o usuário digite o salário inicial do 
funcionário.
"""

def imputnumerocomloop_inteiro(mensagem):
    while True:
        try:
            inp = int(input(mensagem))
            if inp <= 0:
                print('O numero tem que ser maior que zero')
                continue
            return inp
        except ValueError:
            print('Insira um numero inteiro')

salario_inicial = imputnumerocomloop_inteiro('Insira o salario inicial: ')
ano_inicial = 1995
ano_final = 2021

percentual_inicial = 0.015
aumento_percentual = 2

salario_atual = salario_inicial
percentual_atual = percentual_inicial
for ano in range(ano_inicial + 1, ano_final + 1):
    salario_atual *= (1 + percentual_atual)
    percentual_atual *= 2 
    print(f'O salário atual no ano {ano} é de: {salario_atual}')
