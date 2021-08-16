#%% 18 - N, maior, menor e media

"""
Faça um programa que, dado um conjunto de N números, determine o menor 
valor, o maior valor e a soma dos valores.
"""

while True:
    try:
        n = int(input('Insira um numero inteiro N: '))
    except ValueError:
        print('Não foi fornecido um numero inteiro')
    else:
        if n < 0:
            print('numero precisa ser positivo')
        else:
            break

lista_n = []
numero = 0
while True:
    try:
        lista_n.append(float(input('Insira {n} numeros reais, numero {numero}: ')))
    except ValueError:
        print('Deve informar um numero real')
    else:
        numero += 1
        if numero >= n:
            break

soma_n = 0
for i in lista_n:
    soma_n += i

media_n = soma_n/len(lista_n)

maior_n = max(lista_n)   
menor_n = min(lista_n)

print(f'O maior numero é {maior_n}, o menor é {menor_n} e a media é {media_n}')
