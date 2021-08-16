#%% 11-Altere para mostrar soma

"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

while True:
    try:
        num_1 = int(input('Digite um numero inteiro: '))
        num_2 = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('Os Numeros tem que ser inteiros')
    else:
        break

minimo = min(num_1, num_2)
maximo = max(num_1, num_2)

soma = 0
for i in range(minimo + 1, maximo):
    soma += i
    
print(f'Os numeros entre {num_1} e {num_2} é: {soma}')
