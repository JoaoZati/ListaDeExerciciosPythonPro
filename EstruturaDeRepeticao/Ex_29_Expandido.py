#%% 29 - ideia continuar comprando

def continuarcomprando():
    while True:
        try:
            resp = input("Se deseja continuar comprando digite 's' ou 'n': ").upper()
            if resp == 'S':
                return True
            elif resp != 'N':
                print('Favor Digitar "s" ou "n"')
                continue
            return False
        except ValueError:
            print('Ocorreu um erro na digitação')
            
while True:
    try:
        n = int(input('Insira o numero de itens comprados: '))
        if n <= 0 or n > 50:
            print('Numero precisa ser entre 1 e 50')
            continue
        valor_pagar = n*1.99
        if n == 1:
            print(f'O valor a pagar de {n} iten é de: R$ {valor_pagar}')
            if not continuarcomprando():
                break
        print(f'O valor a pagar de {n} itens é de: R$ {valor_pagar}')
        if not continuarcomprando():
            break
    except ValueError:
        print('Não foi fornecido um numero inteiro')
