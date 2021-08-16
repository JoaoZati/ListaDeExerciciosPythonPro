#%% 37 - Academia senso Clientes Refeito

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
maior_peso = codigo_maior_peso = 0
menor_peso = codigo_menor_peso = 0
contagem = 0
soma_peso = 0
soma_altura = 0
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
        
        maior_altura, codigo_maior_altura = comparacao_maior(altura, maior_altura, codigo, codigo_maior_altura)
        menor_altura, codigo_menor_altura = comparacao_menor(altura, menor_altura, codigo, codigo_menor_altura)
        maior_peso, codigo_maior_peso = comparacao_maior(peso, maior_peso, codigo, codigo_maior_peso)
        menor_peso, codigo_menor_peso = comparacao_menor(peso, menor_peso, codigo, codigo_menor_peso)
        
        if contagem == 1:
            menor_altura = altura
            codigo_menor_altura = codigo
            menor_peso = peso
            codigo_menor_peso = codigo
        
        print(f'A media de peso é: {media_peso}')
        print(f'A media de altura é: {media_altura}')
        print(f'O mais alto tem {maior_altura}m e é o aluno {codigo_maior_altura}')
        print(f'O mais baixo tem {menor_altura}m e é o aluno {codigo_menor_altura}')
        print(f'O mais gordo tem {maior_peso}Kg e é o aluno {codigo_maior_peso}')
        print(f'O mais magro tem {menor_peso}Kg e é o aluno {codigo_menor_peso}') 

    except ValueError:
        print('Erro nos valores fornecidos')
