#%% 02 - triangulo crescente

"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n 
inteiro imprima até a n-ésima linha.
"""

def imprimir_triangulo_de_numeros_2(n: int):
    for i in range(1, n + 1):
        for j in range(i):
            print(j+1, end = '   ')
        print('')

imprimir_triangulo_de_numeros_2(4)
