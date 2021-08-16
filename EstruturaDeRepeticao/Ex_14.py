#%% 14 - numero pares e impares

"""
Faça um programa que peça 10 números inteiros, calcule e mostre a 
quantidade de números pares e a quantidade de números impares.
"""
    
lista_10 = []
numero = 1

while True:
    try:
        lista_10.append(int(input('Insira 10 numeros, numero {numero}: ')))
    except ValueError:
        print('Deve informar um numero inteiro')
    else:
        numero += 1
        if numero > 10:
            break

par = 0
impar = 0        
for i in lista_10:
    if i%2 == 0:
        par += 1
    else:
        impar += 1
        
print(f'Você inseriu {par} numeros pares e {impar} numeros impares')
