#%% 40 - Estatistica 5 cidades

"""
Foi feita uma estatística em cinco cidades brasileiras para coletar 
dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
    
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    
Qual o maior e menor índice de acidentes de transito e a que cidade 
pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 
veículos de passeio.
"""

def imputnumerocomloop(mensagem):
    while True:
        try:
            inp = float(input(mensagem))
            if inp <= 0:
                print('O valor tem que ser maior que zero')
                continue
            return inp
        except ValueError:
            print('Insira um numero')
            
def comparacao_maior(valor1, valor2, codigo1, codigo2):
    if valor1 >= valor2:
        return valor1, codigo1
    return valor2, codigo2

def comparacao_menor(valor1, valor2, codigo1, codigo2):
    if valor1 <= valor2:
        return valor1, codigo1
    return valor2, codigo2

maior_indice = codigo_maior_indice = 0
menor_indice = codigo_menor_indice = 0

contagem = 0
soma_indice = soma_carros = 0
while True:
    try:
        codigo = input('Digite a cidade: ')
        indice = imputnumerocomloop('Digite o indice de acidentes de {codigo}: ')
        carros = imputnumerocomloop('Digite o numero de carros de {codigo}: ')
        
        contagem += 1
        soma_indice += indice
        soma_carros += carros
        media_indice = soma_indice/contagem
        media_carros = soma_carros/contagem
        
        maior_indice, codigo_maior_indice = comparacao_maior(indice, maior_indice, codigo, codigo_maior_indice)
        menor_indice, codigo_menor_indice = comparacao_menor(indice, menor_indice, codigo, codigo_menor_indice)
 
        if contagem == 1:
            menor_indice = indice
            codigo_menor_indice = codigo
        
        print(f'A media de indice é: {media_indice}')
        print(f'A media de carros é: {media_carros}')
        print(f'O mais alto indice {maior_indice} e é a cidade {codigo_maior_indice}')
        print(f'O mais baixo indice {menor_indice} e é a cidade {codigo_menor_indice}')
        
        if contagem >= 5:
            break
        
    except ValueError:
        print('Erro nos valores fornecidos')
