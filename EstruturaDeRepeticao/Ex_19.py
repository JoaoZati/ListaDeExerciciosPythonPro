#%% 19 - n só entre 0 a 100

"""
Altere o programa anterior para que ele aceite apenas números entre 
0 e 1000.
"""

lista_n = []
numero = 0

while True:
    try:
        n = int(input('Insira um numero inteiro N: '))
    except ValueError:
        print('Não foi fornecido um numero inteiro')
    else:
        if n < 0 or n > 1000:
            print('numero precisa estar entre 0 e 1000')
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
