#%% 08 - 5 números, soma e média.

"""
Faça um programa que leia 5 números e informe a soma e a média dos 
números.
"""

lista_5 = []
numero = 0

while True:
    try:
        lista_5.append(float(input('Insira 5 numeros, numero {numero}: ')))
    except ValueError:
        print('Deve informar um numero real')
    else:
        numero += 1
        if numero >= 5:
            break

soma_5 = 0
for i in lista_5:
    soma_5 += i

media_5 = soma_5/len(lista_5)   

print(f'A soma do numero é {soma_5} e a media é {media_5}')
