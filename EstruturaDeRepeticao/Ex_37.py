#%% 37 - Academia senso clientes (ERRADO!!!!!)

"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o 
mais alto, o mais baixo, a mais gordo e o mais magro, para isto você 
deve fazer um programa que pergunte a cada um dos clientes da academia 
seu código, sua altura e seu peso. O final da digitação de dados deve 
ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar 
o programa também deve ser informados os códigos e valores do clente 
mais alto, do mais baixo, do mais gordo e do mais magro, além da média 
das alturas e dos pesos dos clientes
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

def comparacao(valor1, valor2, codigo1, codigo2):
    if valor1 >= valor2:
        return valor1, codigo1, valor2, codigo2
    return valor2, codigo2, valor1, codigo1

contagem = 0
soma_peso = 0
soma_altura = 0
antigo_peso = 0
antiga_altura = 0
antigo_codigo = 0
while True:
    try:
        codigo = input('Digite o codigo (digite 0 para sair): ')
        if codigo == '0':
            break
        peso = imputnumerocomloop('Digite o Peso do aluno {codigo}: ')
        altura = imputnumerocomloop('Digite a Altura do aluno {codigo}: ')
        
        contagem += 1
        soma_peso += peso
        soma_altura += altura
        media_peso = soma_peso/contagem
        media_altura = soma_altura/contagem
        maior_peso, codigo_maior_peso, menor_peso, codigo_menor_peso = comparacao(antigo_peso, peso, antigo_codigo, codigo)
        maior_altura, codigo_maior_altura, menor_altura, codigo_menor_altura = comparacao(antiga_altura, altura, antigo_codigo, codigo)
        
        antigo_peso = peso
        antiga_altura = altura
        antigo_codigo = codigo
        
        print(f'A media de peso é: {media_peso}')
        print(f'A media de altura é: {media_altura}')
        if contagem == 1:
            print(f'O mais alto tem {altura}m e é o aluno {codigo}')
            print(f'O mais baixo tem {altura}m e é o aluno {codigo}')
            print(f'O mais gordo tem {peso}Kg e é o aluno {codigo}')
            print(f'O mais magro tem {peso}Kg e é o aluno {codigo}')
            continue
        print(f'O mais alto tem {maior_altura}m e é o aluno {codigo_maior_altura}')
        print(f'O mais baixo tem {menor_altura}m e é o aluno {codigo_menor_altura}')
        print(f'O mais gordo tem {maior_peso}Kg e é o aluno {codigo_maior_peso}')
        print(f'O mais magro tem {menor_peso}Kg e é o aluno {codigo_menor_peso}') 

    except ValueError:
        print('Erro nos valores fornecidos')
