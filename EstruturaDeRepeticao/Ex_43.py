#%% 43 - Cardapio Lanchonete

"""
O cardápio de uma lanchonete é o seguinte:
    
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades 
desejadas. Calcule e mostre o valor a ser pago por item 
(preço * quantidade) e o total geral do pedido. Considere que o cliente 
deve informar quando o pedido deve ser encerrado.
"""

dic_codigo = {'100': 1.20,
              '101': 1.30,
              '102': 1.50,
              '103': 1.20,
              '104': 1.30,
              '105': 1.00,}

dic_codigo_soma = {'100': 0,
                   '101': 0,
                   '102': 0,
                   '103': 0,
                   '104': 0,
                   '105': 0,}

dic_codigo_print = {'100': 'Cachorro Quente',
                    '101': 'Bauru Simples',
                    '102': 'Bauru com ovo',
                    '103': 'Hambúrguer',
                    '104': 'Cheeseburguer',
                    '105': 'Refrigerante',}

def imputcodigo(menssagem):
    while True:
        inp = input(menssagem).lower()
        if inp not in dic_codigo.keys() and inp != 'end':
            print('O codigo não consta no cardapio')
            continue
        return inp

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
            
while True:
    codigo = imputcodigo('Digite o codigo do produto (digite "end" para sair): ')
    if codigo == 'end':
        break
    quantidade = imputnumerocomloop_inteiro('Digite a quantidade do produto: ')
    
    for key, value in dic_codigo.items():
        if codigo == key:
            dic_codigo_soma[key] += quantidade * value
   
total_pagar = 0    
for key, value in dic_codigo_print.items():
    total_pagar += dic_codigo_soma[key]
    print(f'{key}: R$ {dic_codigo_soma[key]}')
    
print(f'Total: R$ {total_pagar}')
