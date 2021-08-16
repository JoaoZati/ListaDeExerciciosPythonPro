#%% 39 - Aluno mais alto mais baixo

"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro 
representando o número do aluno e o segundo representando a sua altura 
em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o 
número do aluno mais alto e o número do aluno mais baixo, junto com 
suas alturas.

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

maior_altura = codigo_maior_altura = 0
menor_altura = codigo_menor_altura = 0
contagem = 1
while True:
    try:
        codigo = input('Digite o codigo (digite 0 para sair): ')
        if codigo == '0':
            break
        peso = imputnumerocomloop('Digite o Peso do aluno {codigo}: ')
        altura = imputnumerocomloop('Digite a Altura do aluno {codigo}: ')
        
        maior_altura, codigo_maior_altura = comparacao_maior(altura, maior_altura, codigo, codigo_maior_altura)
        menor_altura, codigo_menor_altura = comparacao_menor(altura, menor_altura, codigo, codigo_menor_altura)
      
        if contagem == 1:
            menor_altura = altura
            codigo_menor_altura = codigo
            contagem += 1
        
        print(f'O mais alto tem {maior_altura}m e é o aluno {codigo_maior_altura}')
        print(f'O mais baixo tem {menor_altura}m e é o aluno {codigo_menor_altura}')

    except ValueError:
        print('Erro nos valores fornecidos')
