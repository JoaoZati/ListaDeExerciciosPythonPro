#%% 01 - Renzo Exercicio 
"""

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem 
caso o valor seja inválido e continue pedindo até que o usuário informe 
um valor válido.

"""

#numero = int('asdasdfh') # aprender a tratar esses tipos de erros

#usamos o try para evitar esses erros
while True:
    try:
        numero = int(input('Digite um número de 0 a 10: '))
    except ValueError:
        print('Deve ser fornecido um valor inteiro')
    else:
        if 0 <= numero <= 10:
            print(f'Numero infomado é: {numero}')
            break
        else:
            print('O Numero deve estar entre 0 e 10')
