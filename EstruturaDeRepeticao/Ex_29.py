#%% 29 - Loja sr Manoel Joaquin

"""
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, 
com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente 
deve pagar ele desenvolveu um tabela que contém o número de itens que o 
cliente comprou e ao lado o valor da conta. Desta forma a atendente do 
caixa precisa apenas contar quantos itens o cliente está levando e 
olhar na tabela de preços. Você foi contratado para desenvolver o 
programa que monta esta tabela de preços, que conterá os preços de 1 
até 50 produtos, conforme o exemplo abaixo:
    
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
"""


while True:
    try:
        n = int(input('Insira o numero de itens comprados: '))
        if n <= 0 or n > 50:
            print('Numero precisa ser entre 1 e 50')
            continue
        valor_pagar = n*1.99
        if n == 1:
            print(f'O valor a pagar de {n} iten é de: R$ {valor_pagar}')
            break
        print(f'O valor a pagar de {n} itens é de: R$ {valor_pagar}')
        break
    except ValueError:
        print('Não foi fornecido um numero inteiro')
