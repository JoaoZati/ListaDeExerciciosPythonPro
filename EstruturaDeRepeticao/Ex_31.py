#%% 31 - Manuel Joaquin conveniencia

"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 
1,99 e agora possui uma loja de conveniências. Faça um programa que 
implemente uma caixa registradora rudimentar. O programa deverá receber 
um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da 
compra. O programa deve então mostrar o total da compra e perguntar o 
valor em dinheiro que o cliente forneceu, para então calcular e mostrar 
o valor do troco. Após esta operação, o programa deverá voltar ao ponto 
inicial, para registrar a próxima compra. A saída deve ser conforme o 
exemplo abaixo:
    
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...

"""    

soma = 0
n = 1
while True:
    try:
        preco = float(input(f'Produto {n}: R$ '))
        if preco < 0:
            print('Favor digitar apenas valores positivos')
        elif preco == 0:
            break
        soma += preco
        n += 1
    except ValueError:
        print('Favor inserir apenas numeros')
        
print(f'Total: R$ {soma}')
while True:
    try:
        n = int(input('Dinheiro: R$ '))
        if n < soma:
            print('O pagamento tem que ser igual ou maior que a soma')
            continue
        break
    except ValueError:
        print('Não foi fornecido um numero inteiro')

troco = n - soma
print(f'Troco: R$ {troco}')
